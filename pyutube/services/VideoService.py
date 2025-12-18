import os
import sys

from yaspin import yaspin
from yaspin.spinners import Spinners
from pytubefix import YouTube
from pytubefix.cli import on_progress
from termcolor import colored
from moviepy.video.io.ffmpeg_tools import ffmpeg_merge_video_audio

from pyutube.utils import (
    console,
    error_console,
    ask_resolution,
    CANCEL_PREFIX
)





class VideoService:
    def __init__(self, url: str, quality: str, path: str) -> None:
        self.url = url
        self.quality = quality
        self.path = path

    # =========================
    # Search
    # =========================
    def search_process(self) -> YouTube:
        try:
            video = self.__video_search()
        except Exception as error:
            error_console.print(f"❗ Error: {error}")
            sys.exit(1)

        if not video:
            error_console.print("❗ No stream available for the URL.")
            sys.exit(1)

        return video

    @yaspin(
        text=colored("Searching for the video", "green"),
        color="green",
        spinner=Spinners.point,
    )
    def __video_search(self) -> YouTube:
        return YouTube(
            self.url,
            use_oauth=True,
            allow_oauth_cache=True,
            on_progress_callback=on_progress,
        )

    # =========================
    # Streams
    # =========================
    def get_available_resolutions(self, video: YouTube):
        streams = video.streams

        video_streams = streams.filter(
            progressive=False,
            adaptive=True,
            mime_type="video/mp4",
        )

        audio_stream = (
            streams.filter(only_audio=True)
            .order_by("abr")
            .desc()
            .first()
        )

        if not audio_stream:
            error_console.print("❗ No audio stream found.")
            sys.exit(1)

        resolutions_with_sizes = self.get_video_resolutions_sizes(
            video_streams, audio_stream
        )

        resolutions_with_sizes.sort(
            key=lambda x: int(x[0].replace("p", "")) if x[0] else 9999
        )

        resolutions, sizes = zip(*resolutions_with_sizes)
        return list(resolutions), list(sizes), video_streams, audio_stream

    def get_video_streams(self, quality: str, streams):
        if quality.startswith(CANCEL_PREFIX):
            sys.exit(0)

        stream = streams.filter(res=quality).first()

        if not stream:
            available = [int(s.resolution.replace("p", "")) for s in streams]
            target = int(quality.replace("p", ""))
            closest = min(available, key=lambda x: abs(x - target))
            stream = streams.filter(res=f"{closest}p").first()

        return stream

    def get_selected_stream(self, video, is_audio: bool = False):
        resolutions, sizes, streams, audio = self.get_available_resolutions(video)

        if not streams:
            error_console.print("❗ No video streams available.")
            sys.exit(1)

        if not is_audio:
            self.quality = self.quality or ask_resolution(resolutions, sizes)

        if not self.quality and not is_audio:
            sys.exit(0)

        return streams, audio, self.quality

    # =========================
    # Merging (FIXED)
    # =========================
    def merging(self, video_path: str, audio_path: str):
        """
        video_path & audio_path MUST be full paths
        """

        if not os.path.exists(video_path):
            error_console.print(f"❗ Video file not found: {video_path}")
            sys.exit(1)

        if not os.path.exists(audio_path):
            error_console.print(f"❗ Audio file not found: {audio_path}")
            sys.exit(1)

        base_name = os.path.splitext(os.path.basename(video_path))[0]

        temp_output = os.path.join(self.path, f"{base_name}_merged.mp4")
        final_output = os.path.join(self.path, f"{base_name}.mp4")

        try:
            ffmpeg_merge_video_audio(
                video_path,
                audio_path,
                temp_output,
                logger=None,
            )

            # cleanup
            os.remove(video_path)
            os.remove(audio_path)

            # replace safely
            os.replace(temp_output, final_output)

        except Exception as e:
            error_console.print(f"❗ Merge failed: {e}")
            sys.exit(1)

    # =========================
    # Utils
    # =========================
    @staticmethod
    def get_video_resolutions_sizes(available_streams, audio_stream):
        if not available_streams:
            return []

        audio_size = audio_stream.filesize
        results = []

        for stream in available_streams:
            if not stream.resolution:
                continue

            total_size = stream.filesize + audio_size
            mb = total_size / (1024 * 1024)

            results.append(
                (stream.resolution, f"{mb:.2f} MB")
            )

        return results

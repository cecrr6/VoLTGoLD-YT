# 🕵️‍♂️ Examples

> [!IMPORTANT]
> For all commands, the **`[the_download_path]`** is optional. If not specified, the video/audio will be saved in the current working directory.

## **1. Show Version:**

Check the current version of `gold-dl`:

```bash
gold-dl -v
```

## **2. Download Playlists:**

Eager to grab an entire playlist? Just run:

```bash
gold-dl "YOUTUBE_PLAYLIST_LINK" [the_download_path]
```

1. Choose the download format: video or audio.
2. If you select video, pick your desired resolution. For audio, it’ll download everything right away! 🔥

The tool will check all available resolutions from the first video in the playlist and download them in that resolution. 👍

## **3. Download Shorts, Videos, or Audio:**

Ready to download a single short, video, or audio track? Use:

```bash
gold-dl "YOUTUBE_LINK" OR "SHORT_LINK" [the_download_path]
```

1. Select the format: video or audio.
2. If it’s a video, choose the resolution; otherwise, the audio downloads immediately! 🔥

Examples:

```bash
gold-dl youtu.be/cMPnY7EuZvo
gold-dl https://youtube.com/watch?v=cMPnY7EuZvo
```

## **4. Download Audio Immediately:**

Want to grab just the audio? Run:

```bash
gold-dl "YOUTUBE_LINK" OR "SHORT_LINK" [the_download_path] -a
```

Examples:

```bash
gold-dl cMPnY7EuZvo -a
gold-dl -a youtu.be/cMPnY7EuZvo
```

And you’re all set! 🎉

## **5. Download Videos Immediately:**

Need the video fast? Use:

```bash
gold-dl <Y"OUTUBE_LINK" OR "SHORT_LINK" [the_download_path] -f
```

1. Choose your desired resolution.

Examples:

```bash
gold-dl cMPnY7EuZvo -f
gold-dl -f youtu.be/cMPnY7EuZvo
```

Sit back, relax, and enjoy your video! 🎉

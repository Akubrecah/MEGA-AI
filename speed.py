import speedtest

def perform_speed_test():
    """
    Performs an internet speed test using the speedtest-cli library.
    Returns a dictionary with the download speed, upload speed, and ping.
    Speeds are returned in Mbps.
    """
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        download_bps = st.download()
        upload_bps = st.upload()
        ping_ms = st.results.ping

        # Convert bits per second to Mbps
        download_mbps = round(download_bps / 1_000_000, 2)
        upload_mbps = round(upload_bps / 1_000_000, 2)

        return {
            "download_mbps": download_mbps,
            "upload_mbps": upload_mbps,
            "ping_ms": ping_ms
        }
    except Exception as e:
        return {
            "error": str(e)
        }

if __name__ == "__main__":
    result = perform_speed_test()
    if "error" in result:
        print(f"Speed test failed: {result['error']}")
    else:
        print(f"Download Speed: {result['download_mbps']} Mbps")
        print(f"Upload Speed: {result['upload_mbps']} Mbps")
        print(f"Ping: {result['ping_ms']} ms")

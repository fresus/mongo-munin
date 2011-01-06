
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "config":
        doConfig()
    else:
		try:
			port = int(sys.argv[1])
		except (ValueError, IndexError):
			port = DEFAULT_PORT

		doData(port)



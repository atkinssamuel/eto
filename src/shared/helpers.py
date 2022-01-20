def pprint_time_delta(start, end, title=None):
    if title is None:
        print(f"{end - start:0.4f}s")
    else:
        print(f"{title}: {end - start:0.4f}s")

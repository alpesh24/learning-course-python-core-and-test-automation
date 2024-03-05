def pytest_collection_finish(session):
    if session.items:
        quick_tests_count = len([item for item in session.items if not item.get_closest_marker('long_running')])
        long_tests_count = len([item for item in session.items if item.get_closest_marker('long_running')])
        print(f"Collected quick tests: {quick_tests_count}, long-running tests: {long_tests_count}")
    else:
        print(f"Collected quick tests: {0}, long-running tests: {0}")


def pytest_configure(config):
    #register an additional marker
    config.addinivalue_line(
        "markers", "long_running(name): mark test as long-running"
    )
    config.addinivalue_line(
        "markers", "duration(name): mark test as short or long-running"
    )
    config.addinivalue_line(
        "markers", "critical(name): mark test as critical"
    )
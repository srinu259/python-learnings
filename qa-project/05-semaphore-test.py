import threading

class ReadWriteLock:
    def __init__(self):
        self.read_count = 0  # Number of active readers
        self.write_lock = threading.Semaphore(1)  # Ensures exclusive write access
        self.read_lock = threading.Semaphore(1)  # Protects read_count modification

    def acquire_read(self):
        # Protect the reader count
        self.read_lock.acquire()
        self.read_count += 1
        if self.read_count == 1:  # First reader locks the resource for writers
            self.write_lock.acquire()
        self.read_lock.release()

    def release_read(self):
        # Protect the reader count
        self.read_lock.acquire()
        self.read_count -= 1
        if self.read_count == 0:  # Last reader unlocks the resource for writers
            self.write_lock.release()
        self.read_lock.release()

    def acquire_write(self):
        self.write_lock.acquire()  # Writers block all readers and other writers

    def release_write(self):
        self.write_lock.release()


# Example usage:
lock = ReadWriteLock()

# Reader function
def reader(reader_id):
    print(f"Reader {reader_id} wants to read")
    lock.acquire_read()
    print(f"Reader {reader_id} is reading")
    threading.Event().wait(1)  # Simulate read operation
    lock.release_read()
    print(f"Reader {reader_id} finished reading")

# Writer function
def writer(writer_id):
    print(f"Writer {writer_id} wants to write")
    lock.acquire_write()
    print(f"Writer {writer_id} is writing")
    threading.Event().wait(2)  # Simulate write operation
    lock.release_write()
    print(f"Writer {writer_id} finished writing")


# Create threads for demonstration
threads = []
for i in range(3):
    threads.append(threading.Thread(target=reader, args=(i,)))
for i in range(2):
    threads.append(threading.Thread(target=writer, args=(i,)))

# Start and join threads
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
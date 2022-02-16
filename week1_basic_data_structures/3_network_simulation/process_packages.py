# python3

from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []

    def process(self, request):
        # write your code here
        if len(self.finish_time) == 0 or self.finish_time[-1] <= request.arrived_at:
            in_buffer = 0
        else:
            for i in range(0, len(self.finish_time)):
                if self.finish_time[i] > request.arrived_at:
                    # print(f"El finish_time es {self.finish_time[i]} e indice es {i}")
                    index = i
                    break
            # print(f"El indice es {index}")
            in_buffer = len(self.finish_time) - index
        
        # print(f"Buffer: {in_buffer}")
        # print(self.finish_time)
        
        if in_buffer == 0:
            self.finish_time.append(request.arrived_at + request.time_to_process)
            # print(self.finish_time)
            # print("Buffer 0")
            return Response(False, request.arrived_at)
        elif in_buffer >= self.size:
            # print(self.finish_time)
            # print("Buffer copado")
            return Response(True, -1)
        else:
            respuesta = Response(False, self.finish_time[-1])
            self.finish_time.append(self.finish_time[-1] + request.time_to_process)
            # print(self.finish_time)
            # print("Buffer sin problemas")
            return respuesta


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()

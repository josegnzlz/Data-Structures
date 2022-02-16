# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.dictionary = {}
        for i in range(0, bucket_count):
            self.dictionary[i] = []

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        # print(was_found)
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            self.write_chain(cur for cur in reversed(self.dictionary[query.ind]))
        elif query.type == "add":
            position = self._hash_func(query.s)
            try:
                self.dictionary[position].index(query.s)
            except:
                self.dictionary[position].append(query.s)
        elif query.type == "del":
            position = self._hash_func(query.s)
            try:
                self.dictionary[position].remove(query.s)
            except:
                pass
        else:
            position = self._hash_func(query.s)
            try:
                ind = self.dictionary[position].index(query.s)
                # print(f"Indice: {ind}")
            except ValueError:
                ind = -1
                # print(f"Indice: {ind}")
                self.write_search_result(ind != -1)
            else:
                # print(f"Indice: {ind}")
                self.write_search_result(ind != -1)


    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()

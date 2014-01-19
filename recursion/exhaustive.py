from optparse import OptionParser
import copy

def main(array, k):
    result = []

    def combinations(input, output=[]):
        if len(output) == k:
            result.append(output)

        input_lenght = len(input)
        for i in range(input_lenght):
            new_input = copy.deepcopy(input)
            new_output = copy.deepcopy(output)
            new_output.append(new_input[i])
            new_input = new_input[i+1:]
            combinations(new_input, new_output)

    combinations(array)
    return result


print main([1, 2, 3, 4, 5], 3)


# if __name__ == '__main__':
#     parser = OptionParser()
#     (options, args) = parser.parse_args()
#     if args:
#         result = main(args[:-1], int(args[-1]))
#         for r in result:
#             print ', '.join(r)
#     else:
#         print 'insert some args'

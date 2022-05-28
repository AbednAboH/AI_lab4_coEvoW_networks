import matplotlib.pyplot as plt
from Genetic import C_genetic_algorithem
from create_problem_sets import Sorting,network
from settings import *
import time

algo = {1: C_genetic_algorithem}
tags = {1: "GA_CX_SWAP", 2: "ACO", 3: "simulated_annealing", 4: "tabu"}
heuristics = {0: "", 1: "NN", 2: "C&W"}
mutation_index = {1: "rand", 2: "SWAP", 3: "INSERT"}
problem_sets_GA = {1: Sorting,2:network}
inputs_for_testing = ["ackly", "E-n22-k4", "E-n33-k4", "E-n51-k5", "E-n76-k8", "E-n76-k10",
                      "E-n101-k8", "E-n101-k14"]


def plot(fitness, iter, tag, names):
    for i in range(len(fitness)):
        plt.plot(iter[i], fitness[i], label=names[i])
    plt.ylabel('fitness')
    plt.xlabel('iterations')
    plt.title(inputs_for_testing[tag])
    plt.legend()
    plt.show()
    # plt.savefig(f"outputs\{inputs_for_testing[tag]}\{inputs_for_testing[tag]}-iter{len(iter[0])}.png")
    plt.close()


def sort_for_drawing(depth):
    curr=depth[0]
    dep2=[[depth[0]]]
    d=0
    for next in depth[1:]:
        if next[0]<=curr[0]<=next[1] or curr[0] <=next[1]<=curr[1] or next[0]<=curr[1]<=next[1] or curr[0] <=next[0]<=curr[1]:
            dep2.append([next])
            curr=next
            d=d+1
        else:
            dep2[d].append(next)
            curr=next


    return dep2



def plot_network(network):
    index=len(network)
    count=0
    plt.figure(figsize=(10, 7))
    i=0
    j=0
    for depth in network:
        dep=sort_for_drawing(depth)
        print(dep)
        for d in dep:
            for item in d:
                plt.vlines(x=count,ymin=item[0],ymax=item[1],label=str(count))
            count+=1
    # replace 6 with k
    k=6
    for i in range(1,k+1):
        plt.axhline(y=i, color='r', linestyle='-')

    plt.ylabel('comparators')

    plt.xlabel('depth')
    plt.title("network")
    plt.legend()
    # plt.show()
    plt.savefig(f"outputs\graph.png")
    plt.close()
def create_results_file(name):
    file = open(fr"outputs\{name}\script_output.txt", "r")
    f = open(fr"outputs\Results.txt", "a")

    lines = file.readlines()
    lines = [x.split(' ') for x in lines]
    spaceforfirst = 15
    fitnes = 23
    all_lines = fitnes * 3 + spaceforfirst
    for _ in range(all_lines - 2): f.write("-")
    mid = all_lines // 2 - len(name) // 2
    f.write("\n")
    for _ in range(mid): f.write(" ")
    f.write(f"|{name}|")
    f.write("\n| Algorithem   |       fitness         |         Time          |      ticks      |\n")
    for _ in range(all_lines - 2): f.write("-")
    for index, line in enumerate(lines):

        if str(line[0][:2]) == "GA" or line[0][:2] == "TS" or line[0][:2] == "SA" or line[0][:2] == "AC":
            f.write("\n|")
            f.write(str(line[0][:len(line[0]) - 3]))
            for i in range(spaceforfirst - len(line[0]) + 2):
                f.write(" ")
            f.write("|")
        if len(line) > 2 and len(line[2]) > 3:
            print(line)
            if str(line[1]) == ",fittness:":
                f.write(str(line[2]))
                for i in range(fitnes - len(line[2])):
                    f.write(" ")
                f.write("|")
        if len(line) > 3 and len(line[2]) > 3:
            if str(line[4]) == "Time":
                f.write(str(line[7]))
                for i in range(fitnes - len(line[7])):
                    f.write(" ")
                f.write("|")
        if len(line) > 8 and len(line[2]) > 3:
            if str(line[9]) == "ticks:":

                f.write(str(line[10][:len(line[10]) - 3]))
                for i in range(fitnes - len(line[10]) - 3):
                    f.write(" ")
                f.write("|\n")
                for _ in range(all_lines - 2): f.write("-")



def border():
    print("----------------------------------")


def main():
    process = True


    border()
    while process:
        mutation = 1
        border()
        max_iter = int(input("number of iterations:"))
        border()
        # todo: change this one
        #  1. send in target:  k(input) and optimal size of network
        problem_set = problem_sets_GA[1]

        border()
        # target_size = int(input("number of items to sort"))
        target_size = 6
        # GA_POPSIZE = int(input("set population size:"))
        GA_POPSIZE = 100

        GA_TARGET=[6,12]
        solution = C_genetic_algorithem(GA_TARGET, target_size, GA_POPSIZE, problem_set,problem_sets_GA[2],CX_, 0, 3,
                           1, mutation, 1, max_iter=max_iter)

        overall_time = time.perf_counter()
        _,iter,solution=solution.solve()
        plot_network(solution.get_depth())
        overall_time = time.perf_counter() - overall_time
        border()
        print(iter)
        print("Overall runtime :", overall_time)
        border()

        print("\n run again ? press y for yes n for no ")
        if input() == "n":
            process = False


if __name__ == "__main__":
    # selector = int(input("select manual settings or test of all algorithms:\n1: manual  \n2:automatic test"))
    # border()
    main()
    # if selector == 1:
    #     main()
    # else:
    #     border()
    #     popsize = int(input("enter population size for all tests:"))
    #     border()
    #     iterations = int(input("enter  number of max iterations:"))
    #     # test(iterations,popsize)




#
# def ga_script(iterations,popsize):
#     GA_POPSIZE=popsize
#     max_iter=iterations
#     Gene_dist = 4
#
#     names = []
#     select_generator = 1
#     problem_set = problem_sets_GA[select_generator]
#
#     for select_input in range(1,len(inputs.keys())+1):
#         fitness_arr,iter_array=[],[]
#
#         for select_generator in range(1, 3):
#             # cities, cost_matrix, dimentions, capacity = get_sets_from_files(inputs[select_input])
#             cities, cost_matrix, dimentions, capacity = ackley()
#             GA_TARGET = [cities, cost_matrix, dimentions, capacity]
#             target_size = len(cities)
#
#             for mutation in range(2,4):
#
#                 print("GA_I_"+heuristics[select_generator]+"_"+mutation_index[mutation])
#
#                 sol=GA_LAB1(GA_TARGET, target_size, GA_POPSIZE, problem_set, CX_, "fitness", 3,
#                                           1, mutation, Gene_dist,max_iter=max_iter)
#                 fitness,iteration=sol.solve()
#                 fitness_arr.append(fitness)
#                 iter_array.append(iteration)
#                 names.append("GA_I_"+heuristics[select_generator]+"_"+mutation_index[mutation])
#
#                 print("SA_"+heuristics[select_generator]+"_"+mutation_index[mutation])
#
#                 sol = algo[3](GA_TARGET, target_size, GA_POPSIZE, problem_set, "fitness", max_iter, mutation)
#                 fitness, iteration = sol.solve()
#                 fitness_arr.append(fitness)
#                 iter_array.append(iteration)
#                 names.append("SA_"+heuristics[select_generator]+"_"+mutation_index[mutation])
#
#                 print("TS_"+heuristics[select_generator]+"_"+mutation_index[mutation])
#
#                 sol = algo[4](GA_TARGET, target_size, GA_POPSIZE, problem_set, "fitness", max_iter, mutation)
#                 fitness, iteration = sol.solve()
#                 fitness_arr.append(fitness)
#                 iter_array.append(iteration)
#                 names.append("TS_"+heuristics[select_generator]+"_"+mutation_index[mutation])
#
#             print("ACO_" + heuristics[select_generator] )
#
#             sol = algo[2](GA_TARGET, target_size, GA_POPSIZE, problem_set, "fitness", max_iter)
#             fitness, iteration = sol.solve()
#             fitness_arr.append(fitness)
#             iter_array.append(iteration)
#             names.append("ACO_" + heuristics[select_generator] )
#         plot(fitness_arr, iter_array, select_input,names)
#
# def test(iterations,popsize):
#     GA_POPSIZE=popsize
#     max_iter=iterations
#     Gene_dist = 4
#
#     names = []
#     select_generator = 3
#     problem_set = problem_sets_GA[select_generator]
#
#
#     fitness_arr,iter_array=[],[]
#
#     for select_generator in range(0, 1):
#         # cities, cost_matrix, dimentions, capacity = get_sets_from_files(inputs[select_input])
#         for mutation in range(1,2):
#
#             print("GA_I_"+heuristics[select_generator]+"_"+mutation_index[mutation])
#
#             sol=GA_LAB1(GA_TARGET, target_size, GA_POPSIZE, problem_set, 2, "ackly", 3,
#                                       1, mutation, Gene_dist,max_iter=max_iter)
#             fitness,iteration=sol.solve()
#             fitness_arr.append(fitness)
#             iter_array.append(iteration)
#             names.append("GA_I_"+heuristics[select_generator]+"_"+mutation_index[mutation])
#
#             print("SA_"+heuristics[select_generator]+"_"+mutation_index[mutation])
#
#             sol = algo[3](GA_TARGET, target_size, GA_POPSIZE, problem_set, "ackly", max_iter, mutation)
#             fitness, iteration = sol.solve()
#             fitness_arr.append(fitness)
#             iter_array.append(iteration)
#             names.append("SA_"+heuristics[select_generator]+"_"+mutation_index[mutation])
#
#             print("TS_"+heuristics[select_generator]+"_"+mutation_index[mutation])
#
#             sol = algo[4](GA_TARGET, target_size, GA_POPSIZE, problem_set, "ackly", max_iter, mutation)
#             fitness, iteration = sol.solve()
#             fitness_arr.append(fitness)
#             iter_array.append(iteration)
#             names.append("TS_"+heuristics[select_generator]+"_"+mutation_index[mutation])
#
#         print("ACO_" + heuristics[select_generator] )
#
#         sol = algo[2](GA_TARGET, target_size, GA_POPSIZE, problem_set, "acoackly", max_iter,selection=True)
#         fitness, iteration = sol.solve()
#         fitness_arr.append(fitness)
#         iter_array.append(iteration)
#         names.append("ACO_" + heuristics[select_generator] )
#     plot(fitness_arr, iter_array, 0,names)
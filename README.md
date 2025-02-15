# Co-Evolutionary Genetic algorithm Based applied to sorting networks.

## Project Overview

This project is an extension of my previous work, further developing the co-evolutionary approach applied to sorting networks and problem sets. The primary objective is to evolve efficient sorting networks with minimized comparator usage while simultaneously adapting problem sets to enhance the networks' robustness.

## Objectives

- **Co-Evolution Framework**: Expand upon my previous implementation by refining the evolutionary mechanisms governing sorting networks and problem sets.
- **Optimization of Sorting Networks**: Reduce the number of comparators required for sorting while maintaining accuracy.
- **Mutual Adaptation**: Develop problem sets that challenge and improve sorting networks over time.
- **Improved Performance Analysis**: Implement better evaluation metrics and visualization tools to assess co-evolutionary progress.

## How the Algorithm Works

The core of this project is a **Genetic Algorithm (GA)** that drives the co-evolutionary process of sorting networks and problem sets. The algorithm operates as follows:

1. **Initialization**:
   - A population of sorting networks and problem sets is randomly generated.
   - Sorting networks consist of sequences of comparators that define how data elements are sorted.
   - Problem sets include different data sequences that must be sorted.

2. **Evaluation**:
   - Each sorting network is tested against the problem sets.
   - Sorting accuracy and efficiency (number of comparators used) are measured.
   - Problem sets are assessed based on their difficulty in challenging sorting networks.

3. **Selection**:
   - Sorting networks and problem sets undergo **tournament selection**, where the best-performing individuals are chosen to reproduce.
   - Selection ensures that both populations improve over time.

4. **Crossover & Mutation**:
   - **Crossover**: Two parent sorting networks are combined to produce offspring with mixed properties.
   - **Mutation**: Random modifications are introduced to sorting networks and problem sets to encourage exploration and prevent premature convergence.

5. **Replacement & Iteration**:
   - The weakest sorting networks and problem sets are replaced by new offspring.
   - This process repeats for a specified number of generations or until performance plateaus.

6. **Termination**:
   - Evolution stops once sorting networks achieve an optimal balance between efficiency and accuracy.
   - The best sorting networks are stored and can be used for practical applications.

## Implemented Algorithms

The project incorporates several key algorithms:

- **Bubble Sort Network**: A simple sorting network implemented for baseline testing.
- **Bitonic Sort Network**: A more advanced sorting network that sorts data in parallel using predefined comparators.
- **Odd-Even Mergesort Network**: A merge-based sorting network optimized for parallel operations.
- **Insertion Sort Network**: A comparator-based insertion sorting network used in evolutionary comparisons.
- **Quick Sort Network**: A recursive sorting network that adapts to input sequences dynamically.

## Steps to Add a New Algorithm

To integrate a new sorting algorithm into this project, follow these steps:

1. **Define the Algorithm**:
   - Implement the new sorting algorithm in `algorithems.py`.
   - Ensure it follows the expected format for sorting networks.

2. **Integrate into Fitness Functions**:
   - Modify `fitness_functions.py` to incorporate the new algorithm into the evaluation process.
   - Ensure the algorithm is tested against evolving problem sets.

3. **Update Function Selection**:
   - Edit `function_selection.py` to allow the algorithm to be chosen dynamically during evolution.

4. **Modify Selection and Mutation Methods**:
   - Adjust `Selection_methods.py` and `mutations.py` to accommodate the new algorithm.
   - Ensure it can be properly mutated and selected in the evolutionary process.

5. **Test and Validate**:
   - Run the script with different parameters to test the new algorithm.
   - Evaluate its performance through logs and visualizations stored in `outputs/`.

6. **Analyze Results**:
   - Compare the performance of the new algorithm against existing ones.
   - Fine-tune parameters to optimize its efficiency in the evolutionary framework.

## Repository Structure

```
AI_lab4_coEvoW_networks/
│-- main.py
│-- Genetic.py
│-- Selection_methods.py
│-- algorithems.py
│-- create_problem_sets.py
│-- fitness_functions.py
│-- function_selection.py
│-- mutations.py
│-- settings.py
│-- setup.py
│-- requirements.txt
│-- outputs/
│   ├── logs/
│   ├── results/
│-- img.png
```

## Running the Script

### Installation
To run this project, you need to have Python installed along with the required dependencies. Install them using:

```
pip install -r requirements.txt
```

### Running the Evolutionary Process
Execute the script from the command line:

```
python main.py --generations 100 --population_size 50
```

### Command Line Parameters
- `--generations`: Specifies the number of generations the evolution should run for.
- `--population_size`: Defines the size of the population for sorting networks and problem sets.

Example:
```
python main.py --generations 200 --population_size 100
```

## Output and Results
Results will be stored in the `outputs/` directory, including:

- **Logs**: Tracks the progress of each generation.
- **Results**: Stores performance metrics of the evolved sorting networks.
- **Visualizations**: Graphical representation of the evolution process.

Example log snippet:
```
Generation 1: Best fitness = 0.85, Avg fitness = 0.72
Generation 2: Best fitness = 0.88, Avg fitness = 0.74
...
```

## Areas for Improvement

Users can enhance this project in several ways:

- **Fine-tuning Evolutionary Parameters**:
  - Experiment with different mutation rates, crossover probabilities, and selection mechanisms.
- **Extending Fitness Functions**:
  - Introduce more sophisticated evaluation metrics to improve the robustness of evolved sorting networks.
- **Visualizing Evolutionary Progress**:
  - Implement additional visualizations to track changes in sorting efficiency over time.
- **Parallel Processing**:
  - Optimize computational efficiency by parallelizing the evolutionary evaluation process.
- **Generalization Across Sorting Tasks**:
  - Adapt the framework for broader sorting problems beyond predefined problem sets.

## Example Outputs

The `outputs/` directory contains logs and visualizations of the co-evolutionary process. Below is an example of a visualization showing the adaptation of sorting networks over generations:

![16 numbers5_16](https://github.com/user-attachments/assets/0d50172a-1fc9-4629-bb2f-72fae0e1baf7)


This image illustrates how sorting networks and problem sets co-evolve, highlighting the effectiveness of the approach.

## Conclusion

This project builds upon my previous work by implementing a more structured and efficient co-evolutionary framework. Through careful design and testing, it aims to develop highly optimized sorting networks while simultaneously evolving complex problem sets that challenge them. The modular nature of the implementation allows for further expansion and refinement.

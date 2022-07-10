// C program for Kruskal's algorithm to find Minimum
// Spanning Tree of a given connected, undirected and
// weighted graph
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Referencia: https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/
 
struct Edge {
    int src, dest, weight, original_id;
};
 
struct Graph {
    // V-> Number of vertices, E-> Number of edges
    int V, E;

    struct Edge* edge;
};
 
// Creates a graph with V vertices and E edges
struct Graph* createGraph(int V, int E)
{
    struct Graph* graph = (struct Graph*)(malloc(sizeof(struct Graph)));
    graph->V = V;
    graph->E = E;
 
    graph->edge = (struct Edge*)malloc(sizeof( struct Edge) * E);
 
    return graph;
}
 
// A structure to represent a subset for union-find
struct subset {
    int parent;
    int rank;
};
 
// A utility function to find set of an element i
// (uses path compression technique)
int find(struct subset subsets[], int i)
{
    // find root and make root as parent of i
    // (path compression)
    if (subsets[i].parent != i)
        subsets[i].parent
            = find(subsets, subsets[i].parent);
 
    return subsets[i].parent;
}

// A function that does union of two sets of x and y
// (uses union by rank)
void Union(struct subset subsets[], int x, int y, int C)
{
    int xroot = find(subsets, x);
    int yroot = find(subsets, y);
 
    // Attach smaller rank tree under root of high
    // rank tree (Union by Rank)
    // Se modificó para que todos los que se conecten a un nodo con id
    // mayor a C (centro de distribución), tengan el mismo padre, y que no lo pierdan al hacer union
    if (subsets[xroot].parent > C || subsets[yroot].parent > C)
    {
        subsets[xroot].parent = C + 1;
        subsets[yroot].parent = C + 1;
    }
    else if (subsets[xroot].rank < subsets[yroot].rank)
        subsets[xroot].parent = yroot;
    else if (subsets[xroot].rank > subsets[yroot].rank)
        subsets[yroot].parent = xroot;
 
    // If ranks are same, then make one as root and
    // increment its rank by one
    else
    {
        subsets[yroot].parent = xroot;
        subsets[xroot].rank++;
    }
}
 
// Compare two edges according to their weights.
// Used in qsort() for sorting an array of edges
int myComp(const void* a, const void* b)
{
    struct Edge* a1 = (struct Edge*)a;
    struct Edge* b1 = (struct Edge*)b;
    return a1->weight > b1->weight;
}
 
// The main function to construct MST using Kruskal's
// algorithm
void KruskalMST(struct Graph* graph, int C, char* name_file)
{
    int V = graph->V;
    struct Edge
        result[C]; // Tnis will store the resultant MST
    int e = 0; // An index variable, used for result[]
    int i = 0; // An index variable, used for sorted edges
 
    // Step 1: Sort all the edges in non-decreasing
    // order of their weight. If we are not allowed to
    // change the given graph, we can create a copy of
    // array of edges
    qsort(graph->edge, graph->E, sizeof(graph->edge[0]),
        myComp);
 
    // Allocate memory for creating V ssubsets
    struct subset* subsets
        = (struct subset*)malloc(V * sizeof(struct subset));
 
    // Create V subsets with single elements
    for (int v = 0; v < V; ++v) {
        if (v > C)
            subsets[v].parent = C;    
        else
            subsets[v].parent = v;
        subsets[v].rank = 0;
    }
 
    // Number of edges to be taken is equal to V-1
    while (e < V - 1 && i < graph->E) {
        // Step 2: Pick the smallest edge. And increment
        // the index for next iteration
        struct Edge next_edge = graph->edge[i++];
 
        int x = find(subsets, next_edge.src);
        int y = find(subsets, next_edge.dest);
 
        // If including this edge does't cause cycle,
        // include it in result and increment the index
        // of result for next edge
        if (x != y && (x <= C || y <= C)) {
            result[e++] = next_edge;
            Union(subsets, x, y, C);
        }
        // Else discard the next_edge
    }
 
    int minimumCost = 0;
    for (i = 0; i < e; ++i)
    {
        minimumCost += result[i].weight;
    }
    FILE *output_file = fopen(name_file, "w");
    fprintf(output_file, "%d\n", minimumCost);
    //printf("costo: %d \n", minimumCost);
    for (i = 0; i < e; ++i)
    {
        fprintf(output_file, "%d\n", result[i].original_id);
        //printf("id: %d \n", result[i].original_id);
    }
    fclose(output_file);
    free(subsets);
    //printf("Minimum Cost Spanning tree : %d",minimumCost);
    return;
}
 
int main(int argc, char** argv)
{
    if(argc != 3)
    {
        printf("Modo de uso: %s <network.txt> <output.txt>\n", argv[0]);
        return 1;
    }

    FILE *input_file = fopen(argv[1], "r");

    int numero;

    int C, D, H;

    fscanf(input_file, "%d", &C);
    fscanf(input_file, "%d", &D);
    fscanf(input_file, "%d", &H);

    int V = C + D; // Number of vertices in graph
    int E = H; // Number of edges in graph
    struct Graph* graph = createGraph(V, E);
    int index = 0;

    while (H)
	{
    fscanf(input_file, "%d", &numero);
    graph->edge[index].src = numero;
    fscanf(input_file, "%d", &numero);
    graph->edge[index].dest = numero;
    fscanf(input_file, "%d", &numero);
    graph->edge[index].weight = numero;
    graph->edge[index].original_id = index;
    H--;
    index++;
    }
    fclose(input_file);
    
    KruskalMST(graph, C, argv[2]);

    free(graph->edge);

    free(graph);
 
    return 0;
}
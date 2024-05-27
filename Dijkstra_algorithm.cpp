//This program implies dijkstra algorithm to the maze solver problem
//The main idea was taken from this video: https://www.youtube.com/watch?v=a1Z1GmKzcPs&t=697s
//Made by Rustam Rahimov   (211ADB058)
//        Pavlo  Nikolaiev (201ADB090)
//        Mert   Gulmus    (211ADB070)
#include <vector>
#include <iostream>
#include <fstream>
#include <istream>
#include <string>

using namespace std; 
#define INF 9999    //define INF for a constant number for walls or unconnected paths
vector<vector<int>> cost(10201, vector<int>(10201, INF)); //create a vector that will store the adjancency matrix of the maze
vector<int> dist(10201, INF); //contains the distance between numbered node (specific place on a maze) and the start node
bool visited[10201] = {0}; //contains the boolean of whether the specific place on a maze has been visited
int parent[10201]; // creates a path through referencing to the previous node (previous place on a maze)
int des;
int src;


int getNearest(int vertices){ //calculates the nearest place on a maze from a specified place starting from the start node
    int minvalue = INF;
    int minnode = 0;
    for (int i = 0; i < vertices; i++) {
        if(!visited[i] && dist[i]< minvalue) { //if the node wasn't visited and smaller than the minvalue minvalue updates and minnode
            minvalue = dist[i];
            minnode = i;
            }
        }
    return minnode; //returns the closest node
    }

void dijkstra(int src,int vertices) { // the main function of the dijkstra algorithm

    dist[src] = 0; //specifies starting point
    for (int i = 0; i < vertices; i++) {
        int nearest = getNearest(vertices); //finds the closest node
        visited[nearest] = true; //specifies that the node was visited

        for (int adj = 0; adj < vertices; adj++) { //calculates if the adjacent nodes are farther than the nearest node
            if (cost[nearest][adj] != INF && dist[adj] > dist[nearest] + cost[nearest][adj] && cost[nearest][adj]!=INF) {
                dist[adj] = dist[nearest] + cost[nearest][adj]; 
            }
        }
    }
}

int IntLinList(string file_path) { //Main function of this method is to read the given txt file and upon it create an adjacency list and after execute the dijkstra algorithm
    fstream rfile;
    string str;
    rfile.open(file_path, ios::in);//opening file for reading
    if (!rfile.is_open()) { //if file not found
        cout << "No such file found";
    }
    else { //if file found
        std::vector<std::string> data;

        // Read lines from the file and store them in the data vector
        while (std::getline(rfile, str)) {
            data.push_back(str);
        }
        rfile.close(); //closing file
        int cols = data[0].size(); //get dimenstions of the maze
        int rows = cols; //the maze is in shape of square
        if (rows == 0) { //if no data present in txt
            std::cerr << "No data found in file!" << std::endl;
            return 1;
        }


        int count = 0, r = rows - 1;

        for (int i = 0; i < rows; i++) { //calculate the amount of vertices (path choices) + find the starting and ending point
            for (int j = 0; j < cols; j++) {
                if (data[i][j] == 71) { //if the character is "G"
                    des = count;
                    data[i][j] = 48;
                    count++;
                    continue;
                }
                if (data[i][j] == 83) { //if the character is "S"
                    src = count;
                    data[i][j] = 48;
                    count++;
                    continue;
                }
                count++;
            }
        }
        int i = 0, j = 0;
        for (int s = 0; s < count; s++) { //creates the adjacency list
            if (j > r) { //to switch to next row
                i++;
                j = 0;
            }
            if (i == j) { //if adjancency list points to self
                cost[s][s] = 0;
                if (data[i][j] == 88) {
                    j++;
                    continue;
                }
            }
            // the next if statements compute all the possible paths from one place including dioganal
            if (j < r && data[i][j + 1] != 88) { //right
                cost[s][s + 1] = data[i][j + 1] - 48;
            }
            if (i < r && j < r && data[i + 1][j + 1] != 88) { //right-down
                cost[s][s + rows + 1] = data[i + 1][j + 1] - 48;
            }
            if (i < r && data[i + 1][j] != 88) { //down
                cost[s][s + rows] = data[i + 1][j] - 48;
            }
            if (j > 0 && data[i][j - 1] != 88) { //left
                cost[s][s - 1] = data[i][j - 1] - 48;
            }
            if (i < r && j>0 && data[i + 1][j - 1] && data[i + 1][j - 1] != 88) { //left-down
                cost[s][s + rows - 1] = data[i + 1][j - 1] - 48;
            }
            if (i > 0 && data[i - 1][j] && data[i - 1][j] != 88) { //up
                cost[s][s - rows] = data[i - 1][j] - 48;
            }
            if (i > 0 && j < r && data[i - 1][j + 1] && data[i - 1][j + 1] != 88) { //right-up
                cost[s][s - rows + 1] = data[i - 1][j + 1] - 48;
            }
            if (i > 0 && j > 0 && data[i - 1][j - 1] && data[i - 1][j - 1] != 88) { //left-up
                cost[s][s - rows - 1] = data[i - 1][j - 1] - 48;
            }
            j++;
        }
        dijkstra(src, count); //after the adjacency list created, start the dijkstra algorithm
        return count;

    }
};


void display() { // display the final result

        cout << endl;
        cout  << dist[des];
        cout << endl;
}

int main() {
    int c = IntLinList("maze_101x101.txt"); //specify the path
    display();

}
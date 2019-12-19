package homework;

import java.util.ArrayList;

import trees.Node;

public class Homework1 {
	/*
	 * Implement the connected component labeling algorithm. Use 8-neighborhood
	 * definition to define connected components. You should use consecutive
	 * integers (starting with 1) as your labels. Use the following pattern as one
	 * of your input images. This is a 32 x 32 pattern.
	 * 
	 * Image: 
	 * 00000000000000000000001111000000 01001111111111111000000001000000
	 * 01010000000000001001111111111110 01010011111101001001000000000010
	 * 01010100000101001001011111111010 01011001010101001001010000001010
	 * 01000001011101001001010111001010 01001001000001001001010111001010
	 * 01001000111111001001010001001010 01001011100001001111010001001010
	 * 01001100001111000000011111001010 01000000000001000000000000001010
	 * 01111111111111111111111111111010 00000000000000000000000000000010
	 * 00111111111111111111111111000100 00000000000000000000000000111000
	 * 00000111111111111111111110001000 00011111100000000000000001101000
	 * 00100000000000000000000110101000 00100000001111111111110001101000
	 * 00100001110000000000001100001000 00100010000000111110000011001000
	 * 00100100000111111111100001001000 00100100111111111111110011001000
	 * 00100100000000000000000110001000 00100010000000000000000100011000
	 * 00100001111111111111111000111000 00110000000000000000000011111000
	 * 00111100000000000000011111111001 00011111111111111111111111110011
	 * 00000000000000000000000000000111 00000000000000000001111111111111
	 * 
	 * For each input image, show the output image. Hand in your program with input
	 * and output and a brief description of your program and your results in which
	 * you should explain whether your program works correctly and give a brief
	 * description of the approaches and techniques used in your implementation.
	 */

	// Takes in a binary image and returns a labeled group image
	public int[][] labelBinaryImage(int[][] input) {
		// Base Variables
		Node[][] nodeOutput = new Node[input.length][input[0].length];
		int[][] intOutput = new int[input.length][input[0].length];
		Node nullNode = new Node(0);
		Node tempNode;
		int label = 1;
		ArrayList<Node> neighbors = new ArrayList<Node>();
		ArrayList<Integer> hold = new ArrayList<Integer>();

		// Start
		for (int a = 0; a < input.length; a++) {
			// Fill the nodeOutput will nullNode(i.e. 0s);
			for (int b = 0; b < input[a].length; b++) {
				nodeOutput[a][b] = nullNode;
			}

			for (int b = 0; b < input[a].length; b++) {
				// If input array has a 1, check for nearest neighbors
				if (input[a][b] == 1) {
					neighbors = priorNeighbors(b, a, nodeOutput);
					// No neighbors, create new label
					if (neighbors.isEmpty()) {
						tempNode = new Node(label++);
					}
					// Neighbors, use smallest label
					else {
						tempNode = smallestLabel(neighbors);
					}

					// Map the label
					nodeOutput[a][b] = tempNode;

					// Create/combine the hierarchy trees
					for (Node m : neighbors) {
						union(tempNode, m);
					}

				}
			}
		}

		// Run through the 2D array again to update root parents
		for (int a = 0; a < nodeOutput.length; a++) {
			for (int b = 0; b < nodeOutput[a].length; b++) {
				intOutput[a][b] = nodeOutput[a][b].getRootParent().getData();
				// Used to hold each label for reassignment later
				if (hold.contains(intOutput[a][b])) {
					continue;
				} else {
					hold.add(intOutput[a][b]);
				}
			}
		}

		// Removes null value since it will not change
		if (hold.contains(0)) {
			hold.remove(hold.indexOf(0));
		}

		// Updates the 2D integer array to have consecutive labels
		update(intOutput, hold);

		return intOutput;
	}

	// Updates a 2D integer array to have consectuive labels
	public void update(int[][] input, ArrayList<Integer> x) {

		int[] num = new int[x.size()];
		for (int z = 0; z < num.length; z++) {
			num[z] = z + 1;
		}

		for (int a = 0; a < input.length; a++) {
			for (int b = 0; b < input[a].length; b++) {
				if (input[a][b] != 0) {
					int c = 0;
					for (; c < x.size(); c++) {
						if (input[a][b] == x.get(c)) {
							break;
						}
					}
					input[a][b] = num[c];
				}
			}
		}

	}

	// Combines two hierarchy trees together
	public void union(Node x, Node y) {
		Node a = x.getRootParent();
		Node b = y.getRootParent();
		if (a != b) {
			if (y.getParent() == null) {
				x.addChild(y);
			}
			else if (x.getParent() == null) {
				y.addChild(x);
			}
		}
	}

	// Returns the smallest label
	public Node smallestLabel(ArrayList<Node> n) {
		int x = n.get(0).getData();
		Node y = n.get(0);
		for (Node m : n) {
			if (m.getData() < x) {
				x = m.getData();
				y = m;
			}
		}

		return y;
	}

	// Returns true/false if there are possible neighbors
	public boolean possiblePriorNeighbors(int x, int y, Node[][] output) {
		if (output[x - 1][y - 1].getData() != 0 || output[x][y - 1].getData() != 0
				|| output[x + 1][y - 1].getData() != 0 || output[x - 1][y].getData() != 0
				|| output[x + 1][y].getData() != 0 || output[x - 1][y + 1].getData() != 0
				|| output[x + 1][y].getData() != 0 || output[x + 1][y + 1].getData() != 0) {
			return true;
		}

		return false;
	}

	// Returns a list of all neighbors(null if no neighbors)
	// Does not need to check all 8 neighbors since we know that
	// E, SW, S, and SE are all going to be null through processing
	public ArrayList<Node> priorNeighbors(int x, int y, Node[][] output) {
		ArrayList<Node> neighbors = new ArrayList<Node>();

		if (x != 0 && y != 0 && output[y - 1][x - 1].getData() != 0) {
			neighbors.add(output[y - 1][x - 1]);
		}

		if (y != 0 && output[y - 1][x].getData() != 0) {
			neighbors.add(output[y - 1][x]);
		}

		if (y != 0 && x < (output[y].length - 1) && output[y - 1][x + 1].getData() != 0) {
			neighbors.add(output[y - 1][x + 1]);
		}

		if (x != 0 && output[y][x - 1].getData() != 0) {
			neighbors.add(output[y][x - 1]);
		}

		if (x < (output[y].length - 1) && output[y][x + 1].getData() != 0) {
			neighbors.add(output[y][x + 1]);
		}

		return neighbors;
	}

}

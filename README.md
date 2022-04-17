# Digital-image-compression-using-Huffman-encoding-technique
To develop a software algorithm (Huffman encoding) and implement it in order to compress the given
digital image. This lossless compression method utilizes less memory and is widely used across different
applications. 

Huffman Coding First Huffman coding algorithm was developed by David Huffman in 1951. Huffman
coding is an entropy encoding algorithm used for lossless data compression.
###Working of the algorithm with an example:
1. Characters with the highest frequency are encoded with shorter codes than characters that occur less
frequently.
2. Huffman uses the Greedy approach to build a binary tree from the bottom up. Below is an example of
characters and their frequencies. 
3. Create a binary tree with leaf nodes as the frequencies of the characters in increasing order. Create a
new node that stores the sum of frequencies of the smallest 2 nodes below it. 
4. Now repeat the process until only one tree is left having the root node. 
5. Assign ‘0’ to the left child and ‘1’ to the right child while traversing from the root node to the node
having character. 
6. The code word for each source letter is the sequence of labels along the path from the root to the leaf
node representing the letter. 

###PYTHON IMPLEMENTATION OF HUFFMAN ENCODING
1) Read and load the bmp image file using OpenCV and convert it into grayscale.
2) Call a function to calculate and return the frequency dictionary for the pixel values in the image.
3) Build a binary tree using the minimum heap from the frequency table and assign the codes according to
the rule: the highest frequency pixel value will have the shortest length code.
4) Mapping the code words to the corresponding symbols will give the compressed data in binary.
5) Calculate the compression ratio, compression factor, and saving percentage using the input and output
file sizes.

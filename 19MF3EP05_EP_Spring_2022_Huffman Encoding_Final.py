#!/usr/bin/env python
# coding: utf-8

# # Name : Rahul Raghunath Bodanki

# In[1]:


import os     #importing os for file handling
import cv2    #importing cv2 for image handling
import heapq  #importing heapq to create binary tree
import time   #importing time to check time taken to compress



class BinaryTree :
    
    def __init__(self,value,frequ):
        self.value = value
        self.frequ = frequ
        self.left = None
        self.right = None
    
    #initialising the min heap for the binary tree
    
    def __lt__(self,other):
        return self.frequ < other.frequ
    
    def __eq__(self,other):
        return self.frequ == other.frequ
    


class HuffmanCode :
    
    def __init__(self,path):
        
        self.path = path 
        self._heap = []
        
        # _code is a dictionary containing the pixel values and
        #       the huffman codes corresponding to them
        
        self._code = {}
        
    def _pixel_list(self,g_img):
        
        #stores the width and height of the image
        width,height = g_img.shape
        pixel_list = []
        
        #appending each pixel value into a list and returning it
        
        for i in range(width):
            for j in range(height):
                pixel_list.append(g_img[i,j])
                
        return pixel_list
    
    #function to find the frequency of occurence of the pixel values 
    def _frequency_from_text(self,pixels):
        
        frequ_dict = {}
        
        for char in pixels:
            if char not in frequ_dict.keys():
                frequ_dict[char] = 1
            frequ_dict[char] +=1
        
        return frequ_dict
    
    def _Build_heap(self,frequ_dict):
        
        for key in frequ_dict:
            frequency = frequ_dict[key]
            
            binary_tree_node = BinaryTree(key,frequency)
            
            heapq.heappush(self._heap , binary_tree_node)
   
    #creating a binary tree
    def _Build_Binary_Tree(self):
        while len(self._heap)>1:
            binary_tree_node_1 = heapq.heappop(self._heap)
            binary_tree_node_2 = heapq.heappop(self._heap)
            
            sum_of_freq = binary_tree_node_1.frequ + binary_tree_node_2.frequ
            
            newnode = BinaryTree(None,sum_of_freq)
            
            newnode.left = binary_tree_node_1
            newnode.right = binary_tree_node_2
            
            heapq.heappush(self._heap,newnode)
            
        return    
    
    def _Build_Tree_Code_Helper(self,root,curr_bits):
        
        if root is None:
            return
        if root.value is not None:
            self._code[root.value]=curr_bits
            return
        
        self._Build_Tree_Code_Helper(root.left,curr_bits+'0')    #assigning 0 to the left child 
        self._Build_Tree_Code_Helper(root.right,curr_bits+'1')   #assigning 1 to the right child
        
    def _Build_Tree_Code(self):
        root = heapq.heappop(self._heap)
        self._Build_Tree_Code_Helper(root,'')
    
    #storing huffman encoding in encoded_text
    def _Build_Encoded_Text(self,text):
        
        encoded_text=''
        
        for char in text:
            encoded_text += self._code[char]
        
        return encoded_text    
    
    #padding the encoded text
    def _Build_Padded_text(self,encoded_text):
        
        padding_value = 8-len(encoded_text)%8
        
        for i in range(padding_value):
            encoded_text +='0'
            
        padded_info = "{0:08b}".format(padding_value) 
        padded_text = padded_info+encoded_text
        
        return padded_text
    
    #creating a bite array
    def _Build_Bite_Array(self,padded_text):
        
        array=[]
        
        for i in range(0, len(padded_text), 8):
            byte = padded_text[i:i+8]
            array.append(int(byte,2))
                
        return array
    
    #decompressing of the compressed file

    def decompress(self,width, height, ):
        code_read_now = ''
        new_pixel = []
        i=0
        while (i != coding_res.__len__()):
                 
        #Read one later each time
            code_read_now = code_read_now + coding_res[i]
        for key in encoding_table.keys():
                         #If the currently read code exists in the code table 
            if code_read_now == encoding_table[key]: 
                new_pixel. append(key) 
                code_read_now = ' '
                break
        i +=1
        
        #Construct a new image
        decode_image = Image.new( 'L' ,(w,h)) 
        k = 0 
             # 
        for i in range(w):
            for j in range(h):
                decode_image.putpixel((i,j),(int(new_pixel[k]))) 
            k+=1
        decode_image.save(filename+'decoded'+'.bmp') 
        print("Decoding has been completed: the picture is stored")

        
        
    def compression(self):
        
        print("Compression Starting \n")
        #extracting the filename
        filename,file_extension = os.path.splitext(self.path)
        
        output_path = filename + '.bin'
        huffman_encoded_file = filename +'_huffman encoded'+ '.txt'
        
        with open(self.path,'r+') as file , open(output_path,'wb') as output, open(huffman_encoded_file,'w') as output_encoded:
            
            #reading the image using opencv
            img = cv2.imread(path)
            #converting the image into grayscale
            g_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            pixel_values = self._pixel_list(g_img)
            
            #creating text file containing all the pixel values
            with open(filename+'_PIXEL_VALUES.txt', 'w') as f:
                for item in pixel_values:
                    f.write("%s " % item)
            
            #calling frequency function
            frequency_dict = self._frequency_from_text(pixel_values)
            build_heap = self._Build_heap(frequency_dict)
            self._Build_Binary_Tree()
            self._Build_Tree_Code()
            
            encoded_text = self._Build_Encoded_Text(pixel_values)
            padded_text = self._Build_Padded_text(encoded_text)
            
            #converting into binary
            bytes_array = self._Build_Bite_Array(padded_text)
            final_bytes = bytes(bytes_array)
            #creating compressed bin file and text file containing huffman encoding
            output.write(final_bytes)
            output_encoded.write(encoded_text)
            
        print("Compression SUCESSFULL\n")
        print("Huffman Encoding Table containing pixel values and their respective huffman codes ",self._code)
        return output_path
    
    
start = time.time()


path = 's3.bmp'    
h = HuffmanCode(path)
h.compression()


end = time.time()






# In[2]:


#Finding file sizes

file_size = os.path.getsize(path)
print ("Original image file size  ",file_size/1024,"kB")

filename,file_extension = os.path.splitext(path)

output_path = filename + '.bin'
comp_file_size = os.path.getsize(output_path)
print ("Compressed image file size  ",comp_file_size/1024,"kB\n")


#compression ratio


print("Compression ratio = ",file_size/comp_file_size)


# In[3]:


#compression factor

print("Compression factor = ", comp_file_size/file_size)


# In[4]:


#saving persentage

print("Saving percentage = ",(file_size-comp_file_size)/file_size*100)


# In[5]:


#Compression time

print("Time taken to compress a image file = ",end-start,"milliseconds")


# In[ ]:





# In[ ]:





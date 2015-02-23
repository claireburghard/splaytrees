from random import shuffle
import time

class Node: 
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class splayTree:
    def __init__(self):
        self.root = None

    def insert(self, value, parent=None):
        parent = self.root
        if (parent == None):
            #root is null and tree is empty, so begin the tree with this node. 
            self.root = Node(value)
            return
        elif (value < parent.value):
            if (parent.left == None):
                #insert to the left of the parent
                parent.left = Node(value)
                return
            else:
                #search under the left
                self.insert(value, parent.left)
        else:
            if (parent.right == None):
                #insert to the right of the parent
                parent.right = Node(value)
                return
            else:
                #search under the right
                self.insert(value, parent.right)


    def search(self, value, node=None, parent=None, gparent=None, ggparent=None):
        if (node == None):
            #this means that we've just begun the find rountine
            node = self.root #this will keep out place
        if (node == None):
            #it's an empty tree
            return None
        elif (value == node.value):
            #we have found it! That means we have to move some stuff around 
            if (parent != None):
                if (gparent == None):
                    #Zig: swap node with its parent
                    self.rotate(node, parent, gparent)
                elif ((gparent.left == parent and parent.left == node) or 
                      (gparent.right == parent and parent.right == node)):
                    #Zig-zig: swap parent with grandparent 
                    self.rotate(parent, gparent, ggparent)
                    #then swap node with parent
                    self.rotate(node, parent, ggparent)
                else:
                    #Zig-zag: swap node with parent
                    self.rotate(node, parent, ggparent)
                    #then swap node with grandparent
                    self.rotate(node, gparent, ggparent)
            return node 
        elif (value < node.value):
            #search left
            if (node.left !=None):
                leftsearch = self.find(value, node.left, node, parent, gparent)
                if (leftsearch != None):
                    return leftsearch
        elif (value > node.value):
            #search right
            if (node.right != None):
                rightsearch = self.find(value, node.right, node, parent, gparent)
                if rightsearch != None:
                    return rightsearch 
        return None

    def rotate(self, node, parent, gparent):
        if (node == parent.left):
            parent.left = node.right
            node.right = parent
            if (self.root == parent):
                self.root = node
        elif (node == parent.right):
            parent.right = node.left
            node.left = parent
            if (self.root == parent):
                self.root = node
        else:
            print ("rotation not possible")
        if (gparent != None):
            if (gparent.right == parent):
                gparent.right = node
            elif (gp.left == parent):
                gp.left = node


def splay_tree_test(treesize, nsearch):
    #Build the splay tree
    print ("Building your tree...")
    splaytree = splayTree()
    x = [i for i in range(0, treesize)]
    shuffle(x)
    for n in x:
        splaytree.insert(n)
    print ("Done building!")

    #Search the splay tree however many times you asked it to 
    t1 = time.time()
    for i in range(0, nsearch):
        for n in x:
            node = splaytree.search(n)
            if (node == None):
                print ("ERROR")
    t2 = time.time()
    totaltime = t2-t1
    print ("Time:" + str(totaltime))

splay_tree_test(1000, 200)






                


    
 

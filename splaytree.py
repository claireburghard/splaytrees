class Node: 
    def __init__(self,value):
        self.value = val
        self.left = None
        self.right = None

class splayTree:
    def __init__(self):
        self.root = None

    def insert(self, value, parent):
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


    def search(self, value, node, parent, gparent, ggparent):
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





                


    
 

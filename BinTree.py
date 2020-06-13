class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

    def _getData(self):
        return self.data

    def _setData(self, data):
        self.data = data

    def _getLeft(self):
        return self.left

    def _setLeft(self, left):
        self.left = left

    def _getRight(self):
        return self.right

    def _setRight(self, right):
        self.right = right


class BinaryTree:
    def __init__(self, data=None, node=None):
        self.root = None

    def _getRoot(self):
        return self.root

    def insert(self, data):
        # cria um novo nó
        node = Node(data)

        # verifica se a árvore está vazia
        if self.isEmpty():
            self.root = node
        else:
            # árvore não vazia, insere recursivamente
            data_node = None
            curr_node = self.root

            while True:
                if curr_node != None:
                    data_node = curr_node

                    # verifica se vai para esquerda ou direita
                    if node._getData() < curr_node._getData():
                        curr_node = curr_node._getLeft()
                    else:
                        curr_node = curr_node._getRight()
                else:
                    # se curr_node é None, então encontrou onde inserir
                    if node._getData() < data_node._getData():
                        data_node._setLeft(node)
                    else:
                        data_node._setRight(node)
                    break
    
    # verifica se está vazio 
    def isEmpty(self):
        if self.root == None:
            return True
        return False

    # mostra em pré-ordem (raiz-esq-dir)
    def show(self, curr_node):
        try:
            if curr_node != None:
                print('%d' % curr_node._getData(), end=' ')
                self.show(curr_node._getLeft())
                self.show(curr_node._getRight())
        except IndexError as voidIndex:
            print('Value not found {}'.format(voidIndex))

if __name__ == "__main__":
    tree = BinaryTree()
    tree.show(5) # irá apresentar erro, pois não irá encontrar o valor 5 na busca,
                 # levantando um erro no código  de "_getData", pelo fato de não econtar
                 # onde valor foi inserido.
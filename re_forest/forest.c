#include <stdlib.h>
#include <stdio.h>

struct node {
    struct node* left; //f0;
    struct node* right; //f4;
    unsigned char val; //f8;
};

unsigned int check_node(struct node* tree, char* path, char passwd_char);

unsigned int check_tree(struct node* tree, char* path, char* password) {
    unsigned int valid;

    if (!tree || (!path || !password)) {
        return 0;
    } else {
        valid = 1;
        while (*path && *password){
            valid &= check_node(tree, path, *password);
            ++password;
            while ((*path == 'L') || *path == 'R') {
                ++path;
            }
            ++path;
        }
        return valid & (*path & *password);
    }
    return 0;
}

unsigned int check_node(struct node* tree, char* path, char passwd_char) {
    unsigned int res;

    if (!tree || !*path) {
        return 0;
    } else {
        if (tree->val != passwd_char) {
            if (tree->val <= passwd_char) {
                if (*path != 'R') {
                    res = 0;
                } else {
                    res = check_node(tree->right, path + 1, passwd_char);
                }
            } else {
                if (*path != 'L') {
                    res = 0;
                } else {
                    res = check_node(tree->left, path + 1, passwd_char);
                }
            }
        } else {
            if (*path != 'D') {
                res = 0;
            } else {
                if (tree->val != passwd_char) {
                    res = 0;
                } else {
                    res = 1;
                }
            }
        }
    }
    return res;
}

struct node* create_node(struct node* parent, char c) {
    struct node* n;
    struct node* ret;

    if (parent) {
        char val = parent->val;
        if (val >= c) {
            n = create_node(parent->left, c);
            parent->left = n;
            ret = parent;
        } else {
            n = create_node(parent->right, c);
            parent->right = n;
            ret = parent;
        }
    } else {
        n = malloc(12);
        n->left = 0;
        n->right = 0;
        n->val = c;
        ret = n;
    }
    return ret;
}

struct node* build_tree(char* key) {
    struct node* node;
    int offset;  // pointer to char in key
    char c;

    node = 0;
    offset = 0;
    while (key[offset]) {
        c = key[offset];
        node = create_node(node, c);
        ++offset;
    }
    return node;
}

void dump_arcs(struct node *n){
    if(n->left) printf("%c -> %c [label=\" L\"]\n", n->val, n->left->val);
    if(n->right) printf("%c -> %c [label=\" R\"]\n", n->val, n->right->val);

    if(n->left) dump_arcs(n->left);
    if(n->right) dump_arcs(n->right);
}


void dump_dot(char *s, struct node *tree){
    char* c = s;
    printf("digraph BST {\n");
    while(*c != '\0'){
        printf("    %c [ label = \"%c\" ]\n", *c, *c);
	c++;
    }
    dump_arcs(tree);
    printf("}\n");
}

int main(int argc, char** argv) {
    char* key;
    struct node* root;
    char* v7;
    char* arg1;
    char* arg2;
    unsigned int valid;

    key = "yuoteavpxqgrlsdhwfjkzi_cmbn";
    root = build_tree(key);
    if (argc != 3) {
        dump_dot(key, root);
        // printf("You have the wrong number of arguments for this forest.\n");
        // v7 = argv[0];
        // printf("%s [password] [string]\n", v7);
        exit(1);
    }
    arg2 = argv[2];
    arg1 = argv[1];
    valid = check_tree(root, arg2, arg1);
    if (!valid) {
        printf("Nope.\n");
    } else {
        printf("You did it! Submit the input as the flag\n");
    }
    return 0;
}

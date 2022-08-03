import os
import sys

class DecodingAlgorithm:
    # The decoding algorithm is a non-injective function that takes a sequence C
    # back to its decoded form s

    def __init__(self):
        self.decoded_sequence = []
        self.sequence_c = []
        self.input_data = None
        self.re_encoded_sequence = []

    def check_if_file_exists(self,file_to_check):
        # Check if the input file exists
        if os.path.isfile(file_to_check):
            return True
        else:
            return False

    def read_binary_file(self,file_name):
        # Input: file name with the path and name to the binary file
        # Output is the content of the file (as binary)
        file_exists = self.check_if_file_exists(file_name)
        if file_exists:
            with open(file_name, 'rb') as file_binary:
                content_file = file_binary.read()
                self.input_data = content_file
        else:
            print("Warning file does not exists, program is aborted")
            sys.exit(1)

    def create_pairs_from_input_stream(self):
        # Input: input stream from self.input data. Length should be even to build pairs
        # output: sequence of the input stream (p1 q1 p2 q2 pn qn) transformed to [(p_1,q_1),(p_n,q_n)]
        if self.input_data.__len__()%2 == 0:
            for i in range(0,self.input_data.__len__(),2):
                tmp_tupple=(self.input_data[i],self.input_data[i+1])
                self.sequence_c.append(tmp_tupple)
        else:
            # incomplete pairs: the last entry in the input stream should be converted to an invalid pair
            # This is achived by setting q_i to -1
            for i in range(0, self.input_data.__len__()-1, 2):
                tmp_tupple = (self.input_data[i], self.input_data[i + 1])
                self.sequence_c.append(tmp_tupple)
            self.sequence_c.append((0,-1))

    def check_validity_pair(self,pair_to_check):
        # This function checks for valid pairs: 1) p_i = and q_i = c is a valid byte and 2) 0>p_i>=q_i
        if pair_to_check[0]==0 and pair_to_check[1] in range(0,256):
            return True
        elif pair_to_check[0]>0 and pair_to_check[0]>=pair_to_check[1]:
            return True
        else:
            return False

    def decode_sequence(self):
        for x in self.sequence_c:
            # Check if pair is invalid or incomplete
            valid_sequence = self.check_validity_pair(x)
            if valid_sequence:
                # Check if p_i == 0: if so append qi
                if x[0]==0:
                    self.decoded_sequence.append(x[1])
                else:
                    # Read the last p_i characters and append q_i characters
                    last_p_characters = self.decoded_sequence[-x[0]:]
                    sequence_to_append = last_p_characters[:x[1]]
                    self.decoded_sequence.extend(sequence_to_append)
            else:
                self.decoded_sequence.append('3F')


    def re_encode_sequence(self,use_trivial_implementation):
        if use_trivial_implementation == 1:
            # assume p_1 is always 0
            for x in self.decoded_sequence:
                if x != '3F':
                    # the entry is valid --> create a valid pair
                    self.re_encoded_sequence.append((0,x))
                else:
                    # invalid byte so we have to create an invalid pair
                    self.re_encoded_sequence.append((0,-1))
        else:
            return None

    def write_output_to_binary(self,input,output_file_name):
        # output_file_name is the name which will be given to the binairy file
        # convert the list of integers to a byte-like object
        output_bytearray = bytes(input)
        with open(output_file_name, 'wb') as file_to_save:
            file_to_save.write(output_bytearray)
        file_to_save.close()



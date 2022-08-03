from DecodingAlgorithm import DecodingAlgorithm

if __name__ == "__main__":

    # Test 1: this is a test with the input stream 00 20 00 2A 02 02 in hexidecimal notation
    #         This test is successful when the decoding algorithm returns 20 2A 20 (hexidecimal notation)
    print("Perform test with binary test file 1")
    test1 = DecodingAlgorithm()
    test1.read_binary_file(file_name="input_test_1.bin")
    test1.create_pairs_from_input_stream()
    print("The input sequence is %s: " % test1.sequence_c)
    test1.decode_sequence()
    print("Decoded sequence is %s: " % test1.decoded_sequence)
    test1.re_encode_sequence(use_trivial_implementation=1)
    print("The re-encoded sequence is %s" % test1.re_encoded_sequence)
    test1.write_output_to_binary(test1.decoded_sequence,'Standard_Output_test1.bin')
    #test1.write_output_to_binary(test1.re_encoded_sequence,'Standard_Error_test1.bin')
    print("--"*20)

    # Test 2: test where the last element of the input data test 1 is removed
    #         this will give an input data stream which is odd, therefore the last pair should be invalid
    print("Perform test with binary test file 3")
    test3 = DecodingAlgorithm()
    test3.read_binary_file(file_name="input_data_test2.bin")
    test3.create_pairs_from_input_stream()
    print("The input sequence is %s: " % test3.sequence_c)
    test3.decode_sequence()
    print("Decoded sequence is %s: " % test3.decoded_sequence)
    test3.re_encode_sequence(use_trivial_implementation=1)
    print("The re-encoded sequence is %s" % test3.re_encoded_sequence)
    #test3.write_output_to_binary(test3.decoded_sequence, 'Standard_Output_test2.bin')
    #test3.write_output_to_binary(test3.re_encoded_sequence, 'Standard_Error_test2.bin')
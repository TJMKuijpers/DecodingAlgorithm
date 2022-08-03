# DecodingAlgorithm

<p> This repository contains a decoding algorithm that takes a sequence Cs back to its decoded form s.<p>

<h4> The decoding algorithm </h4>
<p>Starting with an empty result bytestring, read the encoded pair sequence (with length n) from the left (i = 0) to the right. For each pair read, if pi = 0, append
qi to the output stream. Otherwise, pi > 0. Read the last pi characters appended to the result string and take the first (from the left) qi characters. </p>

<h4> how to run the python program <h4>
</p> To test the algorithm, you can run the file DecodingalgorithmTest.py. This will start two test: one with a complete input sequence and one test with an odd input sequence. DecodingAlgorithmTest.py will return the input sequence, the decoded sequence, as well as the re-encoded sequence. </p>

<h4> Software requirements </h4>
Python 3.8


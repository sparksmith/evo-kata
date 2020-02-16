# evo-kata
Kata’s are about trying something many times.

Info: 

    -> based on this article: http://codekata.com/kata/kata14-tom-swift-under-the-milkwood/

    -> generate text of a few hundred words. 

    -> Project Gutenberg is a source of online books: https://www.gutenberg.org/


Requirements: 

    -> no UI

    -> Single thread

    -> Unit Testing

    -> Minimum external dependencies 

    -> Input and Output to be FILE based


Assumptions:

    -> Running Python3.8

    -> Ignore punctuation

    -> 1 run of the application creates 1 block of text (paragraph)


Concepts:

Trigram Analysis: 

    There is a sentence: 
        word1 word2 word3 

        word1+word2 form KEYWORD -> save word3 

        if given KEYWORD we can get all the possible word3 that follow. 

    EXAMPLE:
        I wish I may I wish I might 
        I wish -> I I
        wish I -> may might
        may I -> wish
        I may -> I

Generation of new Text:

    CHOOSE an arbitraty word pair for START.

    Appent random possible NEXT WORD to START. 

    When there is no possible sequence STOP. 


    EXAMPLE:
        I may 
        I may I
        I may I wish
        I may I wish I
        I may I wish I may
        I may I wish I may
        I may I wish I may I
        I may I wish I may I wish
        I may I wish I may I wish I 
        I may I wish I may I wish I might*


    ATTENTION:
        You can see that I may occures twice. I will make an assumption that once chosen a WORD3 can be chosen again for KEYWORD, rather than being excluded of the list. 

Problems:

    What do we do if we reach a dead end before the target length ? 


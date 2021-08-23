#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>


/*/GLOBALS
/*
 char array of 1-9
 */
char *ones[] = { "", "one", "two",
    "three", "four","five",
    "six", "seven", "eight", "nine"};

/*
 char array of 10-19
 */
char *tens[] = {"", "ten", "eleven", "twelve",
    "thirteen", "fourteen",
    "fifteen", "sixteen",
    "seventeen", "eighteen", "nineteen"};

/*
 char array of 20-90
 */
char *baseTens[] = {"", "", "twenty", "thirty", "forty", "fifty",
    "sixty", "seventy", "eighty", "ninety"};

/*
 char of 10^n
 */
char *powersOfTen[] = {"hundred", "thousand","million"};

/*
 capital char array of 1-9
 */
char *ones1[] = { "", "ONE", "TWO",
    "THREE", "FOUR","FIVE",
    "SIX", "SEVEN", "EIGHT", "NINE"};

/*
 capital char array of 10-19
 */
char *tens1[] = {"", "TEN", "ELEVEN", "TWELVE",
    "THIRTEEN", "FOURTEEN",
    "FIFTEEN", "SIXTEEN",
    "SEVENTEEN", "EIGHTEEN", "NINETEEN"};

/*
 capital char array of 20-90
 */
char *baseTens1[] = {"", "", "TWENTY", "THIRTY", "FORTY", "FIFTY",
    "SIXTY", "SEVENTY", "EIGHTY", "NINETY"};

/*
 char of 10^n
 */
char *powersOfTen1[] = {"HUNDRED", "THOUSAND","MILLION"};


/*
 changest 9 digit numbers to words using char arrays
 */
void numToWords(char *number)
{
    long numDig = strlen(number) - 1; // number of digits are equal to the length of the char array
    
    while (*number != '\0') // continues while the number isnt null
    {
        
        
        bool prints; // prints is used as a flag to avoid number loss at the end of the triplets/9digits
        
        if(numDig == 9) // if theres a 9th digit
        {
            prints = false; // initializing the flag inside the if instead of the while stops it continously being flagged
            
            printf("%s ", ones[*number - '0']); //prints ascii equivalent of number from ones array
            if(*number - 48 != 0) // if the ascii equivalent of the number isnt 0
            {
                prints = true; // flag
                printf("%s ", powersOfTen[0]); // prints hundred
            }
        }
        
        else if(numDig == 8) // if theres a 8th digit
        {
            if(*number - 48 != 0) // if ascii equivalent of number isnt
            {
                printf("%s ", baseTens[*number - '0']); // prints ascii equivalent of base ten #s
                prints = true; // flag
            }
            
        }
        
        else if(numDig == 7) // if theres a 7th digit
        {
            printf("%s ", ones[*number - '0']); // prints ascii equivalent of number from ones array
            if(*number - 48 != 0) // if ascii equivalent isnt 0
            {
                prints = true; // flag
                
            }
            if(prints) // if true
            {
                printf("%s ", powersOfTen[2]); // prints million
            }
            prints = false; // reset flag
        }
        
        if(numDig == 6) // if theres a 6th digit
        {
            printf("%s ", ones[*number - '0']); //prints ascii equivalent of number from ones array
            if(*number - 48 != 0) // if ascii equivalent isnt 0
            {
                prints = true; // flag
                printf("%s ", powersOfTen[0]); // prints hundred
            }
        }
        
        else if (numDig == 5) // if theres a 5th digit
        {
            if(*number - 48 != 0) // if ascii equivalent isnt 0
            {
                prints = true;
                printf("%s ", baseTens[*number - '0']); // prints ascii equivalent of base ten #s
            }
        }
        
        else if (numDig == 4) // if theres a 4th digit
        {
            printf("%s ", ones[*number - '0']); //prints ascii equivalent of number from ones array
            if(*number - 48 != 0)
            {
                prints = true;
            }
            if(prints)
            {
                printf("%s ", powersOfTen[1]); // prints thousand
            }
            prints = false;
        }
        
        if (numDig == 3) // if theres a 3rd digit
        {
            printf("%s ", ones[*number - '0']); //prints ascii equivalent of number from ones array
            if(*number - 48 != 0)
            {
                printf("%s ", powersOfTen[0]); // prints hundred
            }
        }
        
        else if (numDig == 2) // if theres a 2nd digit
        {
            
            if(*number - 48 > 1)
                printf("%s ", baseTens[*number - '0']); // prints ascii equivalent of base ten #s
            else
            {
                printf("%s ", tens[*number - '0']); // prints ascii equivalent of ten #s
            }
        }
        else if (numDig == 1) // if theres a 1st digit
        {
            
            printf("%s\n ", ones[*number - '0']); //prints ascii equivalent of number from ones array
            
        }
        --numDig; // decrements digit position
        ++number; // increments number
    }


    
}

/*
 turns 2 digit numbers into words (had programs without it but gradescope liked it)
 */
void convertToWords(char *number)
{
    while (*number - '0' <= 19) // while the ascii equivalent is less than or equal to 19
    {
        if (*number == '1') // if number is equal to 1
        {
            int sum = *number - '0' + *(number + 1)- '0'; // creates int of ascii equivalent added to the next position
            printf("%s\n", tens[sum]); // prints this position in tens array
           
            return;
        }
        else if (*number == '2' && *(number + 1) == '0') // if its 20
        {
            printf("twenty\n"); // prints 20
            return;
        }
        else
        {
            int i = *number - 48; // int of number ascii equivalent
            printf("%s ", i? baseTens[i]: ""); // prints ascii equivalent of base ten #s
            ++number;
            if (*number != 48)
                printf("%s ", ones[*number - 48]); // prints ascii equivalent of number from ones array
            return;
        }
    }
}

/*
 changest 9 digit numbers to words using char arrays
 */
void capToWords(char *number)
{
    long numDig = strlen(number) - 1; // number of digits are equal to the length of the char array
    
    
    while (*number != '\0') // continues while the number isnt null
    {
        
        
        bool prints; // prints is used as a flag to avoid number loss at the end of the triplets/9digits
        
        if(numDig == 9) // if theres a 9th digit
        {
            prints = false; // initializing the flag inside the if instead of the while stops it continously being flagged
            
            printf("%s ", ones1[*number - '0']); // prints ascii equivalent of number from ones array
            if(*number - 48 != 0)
            {
                prints = true;
                printf("%s ", powersOfTen1[0]); // prints hundred
            }
        }
        
        else if(numDig == 8) // if theres a 8th digit
        {
            if(*number - 48 != 0)
            {
                printf("%s ", baseTens1[*number - '0']); // prints ascii equivalent of base ten #s
                prints = true;
            }
            
        }
        
        else if(numDig == 7) // if theres a 7th digit
        {
            printf("%s ", ones1[*number - '0']); // prints ascii equivalent of number from ones array
            if(*number - 48 != 0)
            {
                prints = true;
                
            }
            if(prints)
            {
                printf("%s ", powersOfTen1[2]); // prints million
            }
            prints = false;
        }
        
        if(numDig == 6) // if theres a 6th digit
        {
            printf("%s ", ones1[*number - '0']); // prints ascii equivalent of number from ones array
            if(*number - 48 != 0)
            {
                prints = true;
                printf("%s ", powersOfTen1[0]); // prints hundred
            }
        }
        
        else if (numDig == 5) // if theres a 5th digit
        {
            if(*number - 48 != 0)
            {
                prints = true;
                printf("%s ", baseTens1[*number - '0']); // prints ascii equivalent of base ten #s
            }
            
        }
        
        else if (numDig == 4) // if theres a 4th digit
        {
            printf("%s ", ones1[*number - '0']); // prints ascii equivalent of number from ones array
            if(*number - 48 != 0)
            {
                prints = true;
            }
            if(prints)
            {
                printf("%s ", powersOfTen1[1]); // prints thousand
            }
            prints = false;
        }
        
        if (numDig == 3) // if theres a 3rd digit
        {
            printf("%s ", ones1[*number - '0']); // prints ascii equivalent of number from ones array
            if(*number - 48 != 0)
            {
                printf("%s ", powersOfTen1[0]); // hundred
            }
        }
        else if (numDig == 2) // if theres a 2nd digit
        {
            
            if(*number - 48 > 1)
                printf("%s ", baseTens1[*number - '0']); // prints ascii equivalent of base ten #s
            else
            {
                printf("%s ", tens1[*number - '0']);
            }
        }
        else if (numDig == 1)
        {
            printf("%s\n ", ones1[*number - '0']); // prints ascii equivalent of number from ones array
            
        }
        --numDig;
        ++number;
        
    }
    
}



/*
 Main Method
 */
int main(int argc,char **argv)
{
    
    char indica[11]; // creates char array of size 11 (two extra for nulls)
    while(fgets(indica, 11,stdin) != NULL) // while number isnt null
    {
        
        long numDig = strlen(indica) - 1; // creates long number/length of number
        
      
        if(argc > 2) // if there are more then 2 parameters
        {
            printf(stderr, "Cannot have more than two arguments");
            break;
        }
        if(argc == 2) // if there are 2 parameters
        {
            if(*argv[1] == 'u') // if U
            {
                capToWords(indica);
                printf("\n");
            }
            else if (*argv[1] != 'u') // if not U
            {
                printf(stderr, "Not found");
                break;
            }
            
        }
        else if(argc == 1) // if only one argument
        {
            if(numDig == 2) // if only 2 digts
            {
                convertToWords(indica);
            }
            else
            {
                numToWords(indica);
            }
        }
    }
    printf("here");
    return 0;
}
//\

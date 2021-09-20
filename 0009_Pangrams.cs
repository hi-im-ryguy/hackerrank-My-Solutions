using System.CodeDom.Compiler;
using System.Collections.Generic;
using System.Collections;
using System.ComponentModel;
using System.Diagnostics.CodeAnalysis;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Runtime.Serialization;
using System.Text.RegularExpressions;
using System.Text;
using System;

class Result
{

    /*
     * Complete the 'pangrams' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts STRING s as parameter.
     */
     
    static Dictionary<char, bool> ALL_LETTERS_DICTIONARY = new Dictionary<char, bool>()
    {
        {'A', false},
        {'B', false},
        {'C', false},
        {'D', false},
        {'E', false},
        {'F', false},
        {'G', false},
        {'H', false},
        {'I', false},
        {'J', false},
        {'K', false},
        {'L', false},
        {'M', false},
        {'N', false},
        {'O', false},
        {'P', false},
        {'Q', false},
        {'R', false},
        {'S', false},
        {'T', false},
        {'U', false},
        {'V', false},
        {'W', false},
        {'X', false},
        {'Y', false},
        {'Z', false}
    };

    public static string pangrams(string s)
    {
        
        foreach (char character in s)
        {
            try
            {
                if (ALL_LETTERS_DICTIONARY[Char.ToUpper(character)] == false)
                {
                    ALL_LETTERS_DICTIONARY[Char.ToUpper(character)] = true;
                }
            }
            catch (KeyNotFoundException e)
            {
                
            }
        }
        
        string isPangram = "pangram";
        
        foreach (KeyValuePair<char, bool> test in ALL_LETTERS_DICTIONARY) {
            if (test.Value == false)
            {
                isPangram = "not pangram";
                break;   
            }
        }
        return isPangram;
    }

}

class Solution
{
    public static void Main(string[] args)
    {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        string s = Console.ReadLine();

        string result = Result.pangrams(s);

        textWriter.WriteLine(result);

        textWriter.Flush();
        textWriter.Close();
    }
}

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
     * Complete the 'superDigit' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts following parameters:
     *  1. STRING n
     *  2. INTEGER k
     */

    public static int superDigit(string n, int k)
    {
        if (n.Length == 1)
        {
            Console.WriteLine(Int32.Parse(n));
            return Int32.Parse(n);
        }
        
        string digitsString = n;
        
        for (int i = 1; i < k; i++)
        {
            digitsString += n;
        }
        
        Console.WriteLine(digitsString);
        Console.WriteLine(digitsString[0]);
        Console.WriteLine(digitsString.Remove(0, 1));
        return superDigit((superDigit(digitsString[0].ToString(), 0) + superDigit(digitsString.Remove(0, 1), 0)).ToString(), 0);
    }
    
}

class Solution
{
    public static void Main(string[] args)
    {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        string[] firstMultipleInput = Console.ReadLine().TrimEnd().Split(' ');

        string n = firstMultipleInput[0];

        int k = Convert.ToInt32(firstMultipleInput[1]);

        int result = Result.superDigit(n, k);

        textWriter.WriteLine(result);

        textWriter.Flush();
        textWriter.Close();
    }
}

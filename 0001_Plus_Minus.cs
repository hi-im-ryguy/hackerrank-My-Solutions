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
     * Complete the 'plusMinus' function below.
     *
     * The function accepts INTEGER_ARRAY arr as parameter.
     */

    public static void plusMinus(List<int> arr)
    {
        int Positive = 0;
        int Negative = 0;
        int Zero = 0;
        int size = arr.Count;
        
        for (int i = 0; i < size; i++)
        {
            if (arr[i] > 0) Positive++;
            if (arr[i] < 0) Negative++;
            if (arr[i] == 0) Zero++;
        }
        
        float PositiveRatio = (float)Positive/size;
        float NegativeRatio = (float)Negative/size;
        float ZeroRatio = (float)Zero/size;
        
        Console.WriteLine(PositiveRatio.ToString("0.000000"));
        Console.WriteLine(NegativeRatio.ToString("0.000000"));
        Console.WriteLine(ZeroRatio.ToString("0.000000"));
    }

}

class Solution
{
    public static void Main(string[] args)
    {
        int n = Convert.ToInt32(Console.ReadLine().Trim());

        List<int> arr = Console.ReadLine().TrimEnd().Split(' ').ToList().Select(arrTemp => Convert.ToInt32(arrTemp)).ToList();

        Result.plusMinus(arr);
    }
}


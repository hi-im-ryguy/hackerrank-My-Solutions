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
     * Complete the 'timeConversion' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts STRING s as parameter.
     */

    public static string timeConversion(string s)
    {
        string[] words = s.Split(':');
        
        byte hour = Byte.Parse(words[0]);
        byte minute = Byte.Parse(words[1]);
        byte second = Byte.Parse(words[2].Substring(0, 2));
        string period = words[2].Substring(2, 2);
        
        if (period == "PM" & hour != 12)
        {
            hour += 12;
        }
        else if (period == "AM" & hour == 12)
        {
            hour = 0;
        }
        
        string FormattedMilitaryTime = $"{hour.ToString("00")}:{minute.ToString("00")}:{second.ToString("00")}";
        
        Console.WriteLine(FormattedMilitaryTime);
        return FormattedMilitaryTime;
    }

}

class Solution
{
    public static void Main(string[] args)
    {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        string s = Console.ReadLine();

        string result = Result.timeConversion(s);

        textWriter.WriteLine(result);

        textWriter.Flush();
        textWriter.Close();
    }
}

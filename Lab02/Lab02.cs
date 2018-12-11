///----------------------------------------------
///	Lab02.cs
///	Written by Adam Berey for seattle-dsa-501d3
/// in collaboration with Lynn Kuhlman
///	2018-12-10
///----------------------------------------------

using System.Collections.Generic;
using System.Diagnostics;

public class Program
{
	public static void Main()
	{
		var testArr = new int[] {0, 1, 1, 4, 5, 1, -1};
		var tgtArr = new int[] {0, 1, 4, 5, -1};

		var newArr = removeDuplicates(testArr);

		Debug.Assert(newArr == tgtArr);
	}
	
	public static T[] removeDuplicates<T>(T[] arr)
	{
		var newSet = new HashSet<T>();
		
		foreach (T e in arr)
		{
			newSet.Add(e); //if already exists, does nothing
		}
		
		//copy to array to ensure correct return type
		var returnArr = new T[newSet.Count];
		newSet.CopyTo(returnArr);
		
		return returnArr;
	}
}
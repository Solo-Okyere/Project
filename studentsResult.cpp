#include <iostream>
using namespace std;

int main()
{
    int numStudents;

    // Ask for number of students
    cout << "Enter number of students: ";
    cin >> numStudents;

    // Arrays to store data
    string names[numStudents];
    float score1[numStudents], score2[numStudents], score3[numStudents];
    float total[numStudents], average[numStudents];

    float classTotal = 0;
    float highestAvg = -1;
    float lowestAvg = 101;

    // Input student details
    for (int i = 0; i < numStudents; i++)
    {
        cout << "\nEnter name of student " << i + 1 << ": ";
        cin >> names[i];

        // Input scores with validation
        do
        {
            cout << "Enter score for Subject 1: ";
            cin >> score1[i];
        } while (score1[i] < 0 || score1[i] > 100);

        do
        {
            cout << "Enter score for Subject 2: ";
            cin >> score2[i];
        } while (score2[i] < 0 || score2[i] > 100);

        do
        {
            cout << "Enter score for Subject 3: ";
            cin >> score3[i];
        } while (score3[i] < 0 || score3[i] > 100);

        // Calculate total and average
        total[i] = score1[i] + score2[i] + score3[i];
        average[i] = total[i] / 3;

        // Add to class total
        classTotal += average[i];

        // Check highest and lowest average
        if (average[i] > highestAvg)
            highestAvg = average[i];

        if (average[i] < lowestAvg)
            lowestAvg = average[i];
    }

    // Display results
    cout << "\n--- Student Results ---\n";

    for (int i = 0; i < n; i++)
    {
        char grade;

        // Determine grade
        if (average[i] >= 80)
            grade = 'A';
        else if (average[i] >= 70)
            grade = 'B';
        else if (average[i] >= 60)
            grade = 'C';
        else if (average[i] >= 50)
            grade = 'D';
        else
            grade = 'E';

        cout << "\nName: " << names[i];
        cout << "\nTotal: " << total[i];
        cout << "\nAverage: " << average[i];
        cout << "\nGrade: " << grade << endl;
    }

    // Class average
    float classAverage = classTotal / n;

    cout << "\nClass Average: " << classAverage << endl;
    cout << "Highest Average: " << highestAvg << endl;
    cout << "Lowest Average: " << lowestAvg << endl;

    return 0;
}
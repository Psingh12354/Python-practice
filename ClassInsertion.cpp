#include<iostream>
using namespace std;
class InsertionSort{
	public:
		int a[50],i,j,temp,n;
		void insertion()
		{
				cout<<"**** Insertion Sort ****\n\n";
	cout<<"Enter the size of array : ";
	cin>>n;
	cout<<"\n Enter the array elements : \n";
	for(i=0;i<n;i++)
	{
		cin>>a[i];
	}
	for(i=1;i<n;i++)
	{
		temp=a[i];
		j=i-1;
		while((temp<a[j]) && (j>=0))
		{
			a[j+1]=a[j];
			j-=1;
		}
		a[j+1]=temp;
	}
	cout<<"After sorting : \n";
	for(i=0;i<n;i++)
	{
		cout<<a[i];
	}
		}
		
};
int main()
{
	InsertionSort ob;
	ob.insertion();
	return 0;
}

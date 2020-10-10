#include <iostream>
#include <stdlib.h>
#include <malloc.h>
using namespace std;

int erfen_search(int a[],int b,int n)
{
    int left=0,right=n-1,mid;
    if(a[0]==b||a[n-1]==b) return 1;
    for(mid=n/2;left!=right;mid=(left+right)/2)
    {
        if(mid==left||mid==right) break;
        if(b==a[mid]) return 1;
        else if(b<a[mid]) right=mid;
        else if(b>a[mid]) left=mid;
    }
    return 0;
}
void erfen()
{
    int n,m;
    cout<<"输入按照升序排列的序列的大小："<<endl;
    cin>>n;
    if(n<=0||n>10000) exit(0);
    int a[n+1];
    cout<<"输入按照升序排列的序列："<<endl;
    for(int i=0;i<n;i++)
        cin>>a[i];
    cout<<"输入要查询元素的个数："<<endl;
    cin>>m;
    if(m<=0||m>n) exit(0);
    int b[m+1];
    cout<<"输入要查询的元素序列："<<endl;
    for(int i=0;i<m;i++)
        cin>>b[i];
    for(int i=0;i<m;i++)
    {
        if(erfen_search(a,b[i],n))
            cout<<"Yes"<<endl;
        else cout<<"No"<<endl;
    }
}
//输出数组a中的所有元素，从下标0开始
void disp(int a[],int n)
{
    for(int i=0;i<n;i++)
        cout<<a[i]<<endl;
}
void guibing_sort(int a[],int low,int mid,int high)
{
    int *tmpa;  //存储一次排序后的元素序列
    int i=low,j=mid+1,k=0;
    tmpa=(int *)malloc((high-low+1)*sizeof(int));
    while(i<=mid&&j<=high)
    {
        if(a[i]<=a[j])
        {
            tmpa[k]=a[i];
            k++;i++;
        }
        else
        {
            tmpa[k]=a[j];
            k++;j++;
        }
    }
    while(i<=mid)
    {
        tmpa[k]=a[i];
        k++;i++;
    }
    while(j<=high)
    {
        tmpa[k]=a[j];
        k++;j++;
    }
    for(k=0,i=low;i<=high;k++,i++)
        a[i]=tmpa[k];
    free(tmpa);     //释放临时空间
}
void guibing_sort_pass(int a[],int length,int n)
{
    int i;
    for(i=0;i+2*length-1<n;i+=2*length)
        guibing_sort(a,i,i+length-1,i+2*length-1);
    if(i+length-1<n)
        guibing_sort(a,i,i+length-1,n-1);
}
void guibing()
{
    int n;
    cin>>n;
    int a[n+1];
    for(int i=0;i<n;i++)
        cin>>a[i];
    //cout<<"排序前：";disp(a,n);
    int length;
    for(length=1;length<n;length=2*length)
        guibing_sort_pass(a,length,n);
    //cout<<"排序后：";
    disp(a,n);
}
int main()
{
    return 0;
}

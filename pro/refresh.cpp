#include<bits/stdc++.h>
using namespace std;

int main(){
	while (1){
		system("ls>dirs");
		{
			FILE *f=fopen("dirs","r");
			FILE *g=fopen("overview","w");
			char s[2333], t[2333], str[2333];
			
			while (fscanf(f,"%s",s)!=-1){
				if (!isdigit(s[0])) continue;
				
				sprintf(str,"%s/title",s);
				{
					FILE *h=fopen(str,"r");
					if (h!=NULL){
						fscanf(h,"%[^\n]",t);
						fclose(h);
					}else{
						sprintf(t,"untitled");
					}
				}
				fprintf(g,"<p>%s <a href='/prob/%s'>%s</a></p>\n",s,s,t);
			}
			fclose(f);
			fclose(g);
		}
		cerr<<"refreshed"<<endl;
		system("sleep 20");
	}
}

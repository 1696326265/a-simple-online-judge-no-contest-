#include<bits/stdc++.h>
#include<sys/time.h>
using namespace std;

long long gettime(){
	timeval tv;
	gettimeofday(&tv,NULL);
	long long x = tv.tv_sec*1000000ll + tv.tv_usec;
}

char s[2333], str[2333], pid[2333], usn[2333];
double tl;

int main(){
	while (1){
		system("sleep 1");
		system("ls>files");
		{
			FILE *fs=fopen("files","r");
			while (fscanf(fs,"%s",s)!=-1){
				int l=strlen(s);
				if (isdigit(s[0])){
					{
						sprintf(str,"../%s/pid",s);
						FILE *f=fopen(str,"r");
						fscanf(f,"%s",pid);
						fclose(f);
					}
					{
						sprintf(str,"../%s/bel",s);
						FILE *f=fopen(str,"r");
						fscanf(f,"%s",usn);
						fclose(f);
					}
					{
						sprintf(str,"../../pro/%s/tl",pid);
						FILE *f=fopen(str,"r");
						fscanf(f,"%lf",&tl);
						fclose(f);
					}
					long long stim, ttim;
					{
						sprintf(str,"g++ ../%s/x.cpp -o x -O2",s);
						system(str);
						{
							FILE *sh=fopen("fuck.sh","w");
							fprintf(sh,"ulimit -t %.0lf\n",tl+2);
							fprintf(sh,"./x<../../pro/%s/in>out",pid);
							fclose(sh);
							stim=gettime(); system("bash fuck.sh"); ttim=gettime();
						}
					}
					printf(" %s %s %s %lf\n",s,pid,usn,tl);
					{
						sprintf(str,"../%s/ans",s);
						FILE *ans=fopen(str,"w");
						sprintf(str,"diff -b out ../../pro/%s/ans",pid);
						if ((ttim-stim)/1e6>tl||system(str)){
							fprintf(ans,"<h2>Rejected</h2>\n");
							fprintf(ans,"<h3>timeusd : %lf</h3>\n",(ttim-stim)/1e6);
							fprintf(ans,"<h3>the code if from %s</h3>\n",usn);
						}else{
							fprintf(ans,"<h2>Accepted</h2>\n");
							fprintf(ans,"<h3>timeusd : %lf</h3>\n",(ttim-stim)/1e6);
							fprintf(ans,"<h3>the code if from %s</h3>\n",usn);
						}
						fclose(ans);
					}
					
					sprintf(str,"rm %s",s);
					system(str);
					
					break;
				}
			}
			fclose(fs);
		}
	}
}






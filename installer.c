#include <stdio.h>
#include <string.h>

int main()
{
	printf("[?] Do you already installed python? \n>");
	char ans[1];
	scanf("%s", ans);
	if(strcmp(ans, "y") == 0 || strcmp(ans, "Y") == 0){
		printf("[+] Okay :D - Python Skipped\n");
	}
	else {
		system("sudo apt-get install python3");
		system("sudo apt-get install python3-pip");
		printf("[+] Python Installed Successifully!\n");
	}
	printf("Installing Python Libraries...");
	system("pip install time");
	system("pip install requests");
	system("pip install os");
	system("pip install random");
	system("pip install colorama");
	return 0;
}

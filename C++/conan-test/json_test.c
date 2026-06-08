#include "cjson/cJSON.h"
#include <stdlib.h>
#include <stdio.h>


int main(int argc, char** argv)
{
    char verbuf[32];
    snprintf(verbuf,sizeof(verbuf),"%d.%d.%d",CJSON_VERSION_MAJOR,CJSON_VERSION_MINOR,CJSON_VERSION_PATCH);
    cJSON* vj = cJSON_CreateString(verbuf);
    cJSON* rootj = cJSON_CreateObject();
    cJSON_AddItemToObject(rootj,"version",vj);
    char* jstr = cJSON_Print(rootj);
    printf("%s\n",jstr);
    free(jstr);
    cJSON_Delete(rootj);
    return 0;
}

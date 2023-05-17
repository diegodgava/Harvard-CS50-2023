#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height;
    int space;
    int colunas;
    int line;

    do
    {

        height = get_int ("Enter height: ");
    }
    while (height < 0 || height > 8);

    for (line = 0; line < height; line++) {

        for (space = 0; space < height - line - 1; space++)

        {
            printf(" ");
        }

        for (colunas = 0; colunas <= line; colunas++)
        {
            printf("#");
        }
        printf("\n");
    }
}






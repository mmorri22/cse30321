#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>

#define COUT std::cout
#define ENDL std::endl

class first_class{

    private:

        std::string string_1;
        int int_1;
        std::vector<double> vector_1;
        char char_1;
        char char_2;
        double double_1;
        float float_1;
        char char_3;
        std::string string_2;
        std::vector<double> vector_2;

    public:

        // Example Constructor
        first_class() : string_1(), string_2(), vector_1(), vector_2(), double_1(),
            float_1(), int_1(), char_1(), char_2(), char_3() {}

        void print_addresses() const{

            COUT << "Address of first_class is: " << this <<ENDL;
            COUT << "Address of string_1 is   : " << &this->string_1 <<ENDL;
            COUT << "Address of string_2 is   : " << &this->string_2 <<ENDL;
            COUT << "Address of vector_1 is   : " << &this->vector_1 <<ENDL;
            COUT << "Address of vector_2 is   : " << &this->vector_2 <<ENDL;
            COUT << "Address of double_1 is   : " << &this->double_1 <<ENDL;
            COUT << "Address of float_1 is    : " << &this->float_1 <<ENDL;
            COUT << "Address of int_1 is      : " << &this->int_1 <<ENDL;
            //COUT << "Address of char_1 is     : " << &this->char_1 <<ENDL;
            fprintf( stdout, "Address of char_1 is     : %p\n", &this->char_1);
            //COUT << "Address of char_2 is     : " << &this->char_2 <<ENDL;
            fprintf( stdout, "Address of char_2 is     : %p\n", &this->char_2);
            //COUT << "Address of char_3 is     : " << &this->char_3 <<ENDL;
            fprintf( stdout, "Address of char_3 is     : %p\n", &this->char_3);
        }

};

int main(){

    // Create the class
    first_class example_first_class;

    // Print the basic information
    size_t optimal_size = 2*sizeof(std::string) + 2*sizeof(std::vector<double>) 
        + sizeof(int) + sizeof(float) + 3*sizeof(char);
    COUT << "Size of optimal first_class = " << optimal_size << ENDL;
    COUT << "Size of first_class         = " << sizeof(first_class) << ENDL;

    // Print the base addresses
    example_first_class.print_addresses();

    return 0;
}
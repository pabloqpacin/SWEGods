FILES :=                            \
    IDB2.py                     	\
    static/                     	\
    templates/                    	\
    app/models.py					\
    app/tests.py					\
    # app/tests.out					\
 	# IDB2.html						\
 	# IDB2.log						\
 	# IDB2.pdf						\
 	.gitignore						\
 	.travis.yml						\
 	makefile						  


check:
	@not_found=0;                                 \
    for i in $(FILES);                            \
    do                                            \
        if [ -e $$i ];                            \
        then                                      \
            echo "$$i found";                     \
        else                                      \
            echo "$$i NOT FOUND";                 \
            not_found=`expr "$$not_found" + "1"`; \
        fi                                        \
    done;                                         \
    if [ $$not_found -ne 0 ];                     \
    then                                          \
        echo "$$not_found failures";              \
        exit 1;                                   \
    fi;                                           \
    echo "success";

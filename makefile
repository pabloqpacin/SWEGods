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

IDB.log:
	git log > IDB2.log

IDB.html: IDB2.py
	pydoc3 -w IDB2

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

clean:
	rm -f *.pyc
	rm -f IDB2.log

test: IDB.html IDB.log check

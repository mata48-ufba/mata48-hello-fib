a.out:
	gcc fib.c

clean:
	rm fib

test: a.out
	python3 grader.py

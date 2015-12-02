default: run

run:
	@python2 tagfix.py --rename samples/*

inspect:
	@mutagen-inspect samples/*

clean:
	@rm -f samples/*

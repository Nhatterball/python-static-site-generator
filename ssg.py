import typer
from ssg.site import Site

def main(source = "content", dest = "dist"):
    config = {"source": source, "dest" : dest}
    Site(source, dest)

typer.run(main())


if __name__ == "__main__":
    main()
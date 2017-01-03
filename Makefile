CC = gcc
OPTS = -w -g -O0

SRCDIR = ./src
OBJDIR = ./obj
INCDIR = ./include
BINDIR = ./bin
LIBDIR = ./lib

SRCS = $(SRCDIR)/ribbon.c\
$(SRCDIR)/parse.c\
$(SRCDIR)/linkedlist.c\


INCLUDE = $(addprefix -I ,$(INCDIR))
#LINKS =
LIBS = $(addprefix -L, $(LIBDIR))

OBJS = ${SRCS:$(SRCDIR)/%.c=$(OBJDIR)/%.o}

CFLAGS = $(OPTS) $(INCLUDE) $(LIBS) #$(LINKS)

TARGET = $(BINDIR)/Ribbon

all: $(TARGET)

$(TARGET): $(OBJS)
	${CC} -o $@ $(OBJS) ${CFLAGS}

$(OBJS): $(OBJDIR)/%.o : $(SRCDIR)/%.c
	$(CC) -c $< -o $@ $(CFLAGS)

clean:
	rm -f $(OBJS)
cleanall:
	rm -f $(OBJDIR)/*
	rm -f $(BINDIR)/*

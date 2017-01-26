#include <Python.h>


static PyObject *squarefun(PyObject *self, PyObject *args)
{
    int val;

    if (!PyArg_ParseTuple(args, "i", &val))
        return NULL;
    int sq = val * val;
    return Py_BuildValue("i", sq);
}


static PyMethodDef SquareMethods[] = {

    {"squarefun",  squarefun, METH_VARARGS,
     "Sqaure the integer given"},

    {NULL, NULL, 0, NULL}        /* Sentinel */
};


PyMODINIT_FUNC initsquare(void)
{
    (void) Py_InitModule("square", SquareMethods);
}
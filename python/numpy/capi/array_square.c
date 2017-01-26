
#include <Python.h>
#include <numpy/arrayobject.h>



static PyObject* square_func_np(PyObject* self, PyObject* args)
{

    PyArrayObject *in_array;
    PyObject      *out_array;

    /*  parse single numpy array argument */
    // 
    if (!PyArg_ParseTuple(args, "O!", &PyArray_Type, &in_array))
        return NULL;
    // only accept complex 64 = 2 * float32
    if(PyArray_TYPE(in_array) != NPY_COMPLEX64){
        printf("Not a complex64");
        return NULL;
    }

    npy_intp size = PyArray_DIM(in_array, 0);
    
    printf("in the ole functiony poo");
    printf("array size %d \n",size);

    npy_float* data  = (npy_float*)PyArray_DATA(in_array);
    printf("%f %f\n", data[0],data[1]);
    for(npy_intp i = 0; i < size ; i++){
        printf("%f %f\n", data[2*i],data[2*i +1]);
    }

    /*  construct the output array, like the input array */
    out_array = PyArray_NewLikeArray(in_array, NPY_ANYORDER, NULL, 0);
    if (out_array == NULL)
        return NULL;

    Py_INCREF(out_array);
    return out_array;

    /*  in case bad things happen */
    fail:
        Py_XDECREF(out_array);
        return NULL;
}

/*  define functions in module */
static PyMethodDef SquareMethods[] =
{
     {"square_func_np", square_func_np, METH_VARARGS,
         "evaluate the cosine on a numpy array"},
     {NULL, NULL, 0, NULL}
};

/* module initialization */
PyMODINIT_FUNC
initarray_square(void)
{
     (void) Py_InitModule("array_square", SquareMethods);
     /* IMPORTANT: this must be called */
     import_array();
}
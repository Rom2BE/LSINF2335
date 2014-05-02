import java.lang.reflect.Method;
...
    public Object callCompare(Object o, String s1, String s2) {
        Class cls = o.getClass();
        try {
            Method method = cls.getMethod("compare", String.class, String.class);
            return method.invoke(o, s1, s2);
        }
        [multiple catch clauses: NoSuchMethodException, IllegalAccessException, IllegalArgumentException, InvocationTargetException...]

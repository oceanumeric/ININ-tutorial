# ININ-tutorial

1. Click the button below to create a new repository from this template

   [![Use this template](https://img.shields.io/badge/Use%20this%20template-2ea44f?style=for-the-badge&logo=github)]

2. Setup profile

   - Go to `Settings` -> `Profile` -> `Import profile` 
   - paste the following link to `Import profile` and click `Import`

   ```bash
   https://gist.github.com/oceanumeric/272357d747a18013baa370ac215c6721
   ```

   Once imported, you should see the following profile:

 

3. In the terminal, run

```
LC_ALL=C.UTF-8 jupyter notebook --allow-root
```

Then select the jupyer kernel from the running session.


For someone runs R in a docker environment (under root), try to run R with below command,

```
LC_ALL=C.UTF-8 R
# instead of just `R`
```

**Remark**: we need this as the we encounter an error from `SPARQL` package in R, which is due to the locale setting (causes the xml parsing error).

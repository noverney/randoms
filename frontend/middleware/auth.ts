import { collection, doc, setDoc } from "firebase/firestore"
import { getCurrentUser } from "vuefire"

export default defineNuxtRouteMiddleware(async (to, from) => {
    const user = await getCurrentUser()

    // redirect the user to the login page
    if (!user) {
        return navigateTo({
            path: '/login',
            query: {
                redirect: to.fullPath,
            },
        })
    } else {
        // redirect user on first sign up and init user document
        const firestore = useFirestore()
        const me = useDocument(doc(collection(firestore, 'users'), user.uid))

        if (!me.value) {
            console.log("adddoc")
            await setDoc(doc(firestore, "users", user.uid), {
                name: user.displayName,
                preferences: {},
                days: [],
            });
        }
    }
})
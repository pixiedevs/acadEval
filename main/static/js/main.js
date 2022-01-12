const store = PetiteVue.reactive({
    state: {
        message: {
            show: false, desc: "Welcome",
            toggle(show = null) {
                if (show == null)
                    this.show = !this.show;
                else
                    this.show = show;
                return this.show;
            },
            set(desc = null) {
                if (desc != null) {
                    this.desc = desc;
                }
                this.toggle(true);
                setTimeout(() => {
                    this.toggle(false);
                }, 2000);
            }
        },
        attendance: {
            data: { attendance: null, present: 0, absent: 0 },
            show: true,
            async fetch() {
                await axios.get('/student/attendance',
                    { params: { type: "api", sem: document.getElementById("sem").value, month: document.getElementById("month").value } })
                    .then((response) => {
                        this.data = response.data;
                        if (this.data == '') {
                            this.show = false;
                            if(chart) chart.destroy();
                        }
                        else {
                            this.show = true;
                            this.data.percentage = Math.floor((this.data.present * 100) / (this.data.absent + this.data.present));
                            document.querySelector("canvas").setAttribute("data", (this.data.present + ', ' + this.data.absent));
                            createCharts();
                        }
                    })
            }
        },
        marks: {},
        library: {},
        updatedAt: Date()
    },
    getState() {
        try {
            if (sessionStorage.storeState)
                this.state = JSON.parse(sessionStorage.storeState);
        } catch {
            sessionStorage.storeState = ''
            this.state.message = "can't restore state"
        }
    },
    saveState() {
        sessionStorage.storeState = JSON.stringify(this.state);
    },
    setter: {
    },
    methods: {
    }
})

store.getState();

PetiteVue.
    createApp({
        $delimiters: ['{', '}'],
        store
    }).mount("#inBody");

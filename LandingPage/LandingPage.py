import reflex as rx
from rxconfig import config

class State(rx.State):
    """The app state."""
    ...

def index() -> rx.Component:
    return rx.scroll_area(
        rx.box(
            rx.vstack(
                # NAVBAR
                rx.hstack(
                    rx.image(src="/DuskUI.ico", width="55px", height="auto"),
                    rx.heading("DuskUI", align="left", size="5", padding="16px"),
                    rx.spacer(),
                    rx.text("Products", padding="8px"),
                    rx.text("Features", padding="8px"),
                    rx.text("Pricing", padding="8px"),
                    rx.text("Support", padding="8px"),
                    rx.text(
                        "Start free trial",
                        padding="12px",
                        border="1px solid #666",
                        border_radius="8px"
                    ),
                    spacing="4",
                    width="100%",
                ),

                # HERO SECTION
                rx.hstack(
                    rx.box(
                        rx.heading(
                            "Connecting Devs with Employers",
                            size="9",
                            width="100%",
                            align="left"
                        ),
                        rx.text(
                            "Amet minim mollit non deserunt ullamco est sit aliqua dolor do amet sint. "
                            "Velit officia consequat duis enim velit mollit. Exercitation veniam consequat.",
                            size="3",
                            margin_top="8px"
                        ),
                        rx.hstack(
                            rx.button(
                                "Get Started",
                                bg="#3b82f6",
                                color="white",
                                padding="12px 24px",
                                border_radius="8px",
                                margin_top="24px"
                            ),
                            rx.button(
                                "Learn More",
                                bg="transparent",
                                color="white",
                                border="1px solid #666",
                                padding="12px 24px",
                                border_radius="8px",
                                margin_top="24px"
                            ),
                            spacing="4"
                        ),
                        spacing="4",
                        width="50%",
                        padding="32px"
                    ),
                    rx.box(
                        rx.image(
                            src="https://landingfoliocom.imgix.net/store/collection/dusk/images/hero/2/illustration.png",
                            width="450px",
                            height="auto"
                        ),
                        width="50%",
                        display="flex",
                        justify_content="center",
                        align_items="center"
                    ),
                    width="100%",
                    align="center"
                ),

                # SEARCH BAR
                rx.badge(
                    rx.flex(
                        rx.icon("search", size=18),
                        rx.text(
                            "Search documentation...",
                            size="3",
                            weight="medium",
                        ),
                        direction="row",
                        gap="1",
                        align="center",
                    ),
                    size="2",
                    radius="full",
                    color_scheme="gray",
                    margin_top="32px"
                ),

                # FEATURES SECTION
                rx.box(
                    rx.heading("Why Choose DuskUI?", size="8", text_align="center", margin_bottom="32px"),
                    rx.grid(
                        rx.box(
                            rx.icon("zap", size=32, color="#3b82f6", margin_bottom="16px"),
                            rx.heading("Lightning Fast", size="5", margin_bottom="8px"),
                            rx.text(
                                "Built with performance in mind. Our platform connects developers "
                                "with opportunities in seconds, not hours.",
                                size="3",
                                color="#888"
                            ),
                            padding="24px",
                            border="1px solid #333",
                            border_radius="12px",
                            text_align="center"
                        ),
                        rx.box(
                            rx.icon("shield", size=32, color="#10b981", margin_bottom="16px"),
                            rx.heading("Secure & Trusted", size="5", margin_bottom="8px"),
                            rx.text(
                                "Enterprise-grade security ensures your data and connections "
                                "remain safe and private at all times.",
                                size="3",
                                color="#888"
                            ),
                            padding="24px",
                            border="1px solid #333",
                            border_radius="12px",
                            text_align="center"
                        ),
                        rx.box(
                            rx.icon("users", size=32, color="#f59e0b", margin_bottom="16px"),
                            rx.heading("Global Network", size="5", margin_bottom="8px"),
                            rx.text(
                                "Access to thousands of verified employers and developers "
                                "from around the world, all in one place.",
                                size="3",
                                color="#888"
                            ),
                            padding="24px",
                            border="1px solid #333",
                            border_radius="12px",
                            text_align="center"
                        ),
                        columns="3",
                        spacing="4",
                        width="100%"
                    ),
                    padding="64px 32px",
                    width="100%"
                ),

                # STATS SECTION
                rx.box(
                    rx.hstack(
                        rx.box(
                            rx.heading("10K+", size="8", color="#3b82f6"),
                            rx.text("Active Developers", size="3", color="#888"),
                            text_align="center"
                        ),
                        rx.box(
                            rx.heading("500+", size="8", color="#10b981"),
                            rx.text("Partner Companies", size="3", color="#888"),
                            text_align="center"
                        ),
                        rx.box(
                            rx.heading("95%", size="8", color="#f59e0b"),
                            rx.text("Success Rate", size="3", color="#888"),
                            text_align="center"
                        ),
                        rx.box(
                            rx.heading("24/7", size="8", color="#ef4444"),
                            rx.text("Support Available", size="3", color="#888"),
                            text_align="center"
                        ),
                        spacing="8",
                        width="100%",
                        justify="center"
                    ),
                    padding="48px 32px",
                    bg="#111",
                    border_radius="12px",
                    margin="32px 0"
                ),

                # HOW IT WORKS SECTION
                rx.box(
                    rx.heading("How It Works", size="8", text_align="center", margin_bottom="48px"),
                    rx.hstack(
                        rx.box(
                            rx.box(
                                rx.text("1", size="4", weight="bold"),
                                bg="#3b82f6",
                                color="white",
                                width="64px",
                                height="64px",
                                border_radius="50%",
                                display="flex",
                                align_items="center",
                                justify_content="center",
                                margin_bottom="16px",
                                margin_x="auto"
                            ),
                            rx.heading("Create Profile", size="5", margin_bottom="8px"),
                            rx.text(
                                "Set up your professional profile with skills, experience, "
                                "and portfolio showcase.",
                                size="3",
                                color="#888",
                                text_align="center"
                            ),
                            text_align="center",
                            width="30%"
                        ),
                        rx.box(
                            rx.box(
                                rx.text("2", size="4", weight="bold"),
                                bg="#10b981",
                                color="white",
                                width="64px",
                                height="64px",
                                border_radius="50%",
                                display="flex",
                                align_items="center",
                                justify_content="center",
                                margin_bottom="16px",
                                margin_x="auto"
                            ),
                            rx.heading("Get Matched", size="5", margin_bottom="8px"),
                            rx.text(
                                "Our AI algorithm matches you with relevant opportunities "
                                "based on your skills and preferences.",
                                size="3",
                                color="#888",
                                text_align="center"
                            ),
                            text_align="center",
                            width="30%"
                        ),
                        rx.box(
                            rx.box(
                                rx.text("3", size="4", weight="bold"),
                                bg="#f59e0b",
                                color="white",
                                width="64px",
                                height="64px",
                                border_radius="50%",
                                display="flex",
                                align_items="center",
                                justify_content="center",
                                margin_bottom="16px",
                                margin_x="auto"
                            ),
                            rx.heading("Start Working", size="5", margin_bottom="8px"),
                            rx.text(
                                "Connect directly with employers and begin your next "
                                "exciting project or career opportunity.",
                                size="3",
                                color="#888",
                                text_align="center"
                            ),
                            text_align="center",
                            width="30%"
                        ),
                        spacing="5",
                        width="100%",
                        justify="center",
                        align="start"
                    ),
                    padding="64px 32px",
                    width="100%"
                ),

                # TESTIMONIALS SECTION
                rx.box(
                    rx.heading("What Our Users Say", size="8", text_align="center", margin_bottom="48px"),
                    rx.grid(
                        rx.box(
                            rx.text(
                                "\"DuskUI transformed my career search. Within a week, I had three "
                                "interviews lined up with top tech companies.\"",
                                size="3",
                                style={"font-style": "italic"},
                                margin_bottom="16px"
                            ),
                            rx.hstack(
                                rx.avatar(fallback="JS", size="3"),
                                rx.box(
                                    rx.text("John Smith", weight="bold", size="3"),
                                    rx.text("Frontend Developer", size="2", color="#888")
                                ),
                                spacing="3"
                            ),
                            padding="24px",
                            border="1px solid #333",
                            border_radius="12px"
                        ),
                        rx.box(
                            rx.text(
                                "\"As a recruiter, DuskUI helps me find qualified candidates "
                                "faster than any other platform I've used.\"",
                                size="3",
                                style={"font-style": "italic"},
                                margin_bottom="16px"
                            ),
                            rx.hstack(
                                rx.avatar(fallback="MD", size="3"),
                                rx.box(
                                    rx.text("Maria Davis", weight="bold", size="3"),
                                    rx.text("Tech Recruiter", size="2", color="#888")
                                ),
                                spacing="3"
                            ),
                            padding="24px",
                            border="1px solid #333",
                            border_radius="12px"
                        ),
                        rx.box(
                            rx.text(
                                "\"The platform's AI matching is incredibly accurate. "
                                "I found my dream job in just two weeks!\"",
                                size="3",
                                style={"font-style": "italic"},
                                margin_bottom="16px"
                            ),
                            rx.hstack(
                                rx.avatar(fallback="AL", size="3"),
                                rx.box(
                                    rx.text("Alex Lee", weight="bold", size="3"),
                                    rx.text("Full Stack Developer", size="2", color="#888")
                                ),
                                spacing="3"
                            ),
                            padding="24px",
                            border="1px solid #333",
                            border_radius="12px"
                        ),
                        columns="3",
                        spacing="4",
                        width="100%"
                    ),
                    padding="64px 32px",
                    width="100%"
                ),

                # PRICING SECTION
                rx.box(
                    rx.heading("Choose Your Plan", size="8", text_align="center", margin_bottom="48px"),
                    rx.hstack(
                        rx.box(
                            rx.heading("Free", size="6", margin_bottom="16px"),
                            rx.heading("$0", size="8", color="#3b82f6", margin_bottom="8px"),
                            rx.text("per month", size="2", color="#888", margin_bottom="24px"),
                            rx.vstack(
                                rx.text("✓ Basic profile creation", size="3"),
                                rx.text("✓ Up to 5 applications", size="3"),
                                rx.text("✓ Community support", size="3"),
                                rx.text("✓ Standard matching", size="3"),
                                spacing="2",
                                align="start",
                                margin_bottom="24px"
                            ),
                            rx.button(
                                "Get Started",
                                bg="transparent",
                                color="white",
                                border="1px solid #3b82f6",
                                width="100%",
                                padding="12px"
                            ),
                            padding="32px",
                            border="1px solid #333",
                            border_radius="12px",
                            text_align="center",
                            width="30%"
                        ),
                        rx.box(
                            rx.heading("Pro", size="6", margin_bottom="16px"),
                            rx.heading("$29", size="8", color="#10b981", margin_bottom="8px"),
                            rx.text("per month", size="2", color="#888", margin_bottom="24px"),
                            rx.vstack(
                                rx.text("✓ Everything in Free", size="3"),
                                rx.text("✓ Unlimited applications", size="3"),
                                rx.text("✓ Priority support", size="3"),
                                rx.text("✓ Advanced AI matching", size="3"),
                                rx.text("✓ Profile analytics", size="3"),
                                spacing="2",
                                align="start",
                                margin_bottom="24px"
                            ),
                            rx.button(
                                "Start Pro Trial",
                                bg="#10b981",
                                color="white",
                                width="100%",
                                padding="12px"
                            ),
                            padding="32px",
                            border="2px solid #10b981",
                            border_radius="12px",
                            text_align="center",
                            width="30%",
                            position="relative",
                            transform="scale(1.05)"
                        ),
                        rx.box(
                            rx.heading("Enterprise", size="6", margin_bottom="16px"),
                            rx.heading("Custom", size="8", color="#f59e0b", margin_bottom="8px"),
                            rx.text("pricing", size="2", color="#888", margin_bottom="24px"),
                            rx.vstack(
                                rx.text("✓ Everything in Pro", size="3"),
                                rx.text("✓ Dedicated account manager", size="3"),
                                rx.text("✓ Custom integrations", size="3"),
                                rx.text("✓ Bulk hiring tools", size="3"),
                                rx.text("✓ SLA guarantee", size="3"),
                                spacing="2",
                                align="start",
                                margin_bottom="24px"
                            ),
                            rx.button(
                                "Contact Sales",
                                bg="transparent",
                                color="white",
                                border="1px solid #f59e0b",
                                width="100%",
                                padding="12px"
                            ),
                            padding="32px",
                            border="1px solid #333",
                            border_radius="12px",
                            text_align="center",
                            width="30%"
                        ),
                        spacing="4",
                        width="100%",
                        justify="center"
                    ),
                    padding="64px 32px",
                    width="100%"
                ),

                # FAQ SECTION
                rx.box(
                    rx.heading("Frequently Asked Questions", size="8", text_align="center", margin_bottom="48px"),
                    rx.vstack(
                        rx.box(
                            rx.heading("How does the matching algorithm work?", size="4", margin_bottom="8px"),
                            rx.text(
                                "Our AI-powered matching system analyzes your skills, experience, preferences, "
                                "and career goals to connect you with the most relevant opportunities. It learns "
                                "from successful matches to continuously improve recommendations.",
                                size="3",
                                color="#888"
                            ),
                            padding="24px",
                            border="1px solid #333",
                            border_radius="8px",
                            width="100%"
                        ),
                        rx.box(
                            rx.heading("Is DuskUI free to use?", size="4", margin_bottom="8px"),
                            rx.text(
                                "Yes! We offer a free plan that includes basic profile creation, up to 5 applications "
                                "per month, and access to our community. Premium plans offer additional features "
                                "like unlimited applications and priority support.",
                                size="3",
                                color="#888"
                            ),
                            padding="24px",
                            border="1px solid #333",
                            border_radius="8px",
                            width="100%"
                        ),
                        rx.box(
                            rx.heading("How quickly can I expect to hear back from employers?", size="4", margin_bottom="8px"),
                            rx.text(
                                "Response times vary by employer, but our users typically hear back within 3-5 business days. "
                                "Premium users with complete profiles and relevant skills often see faster response rates.",
                                size="3",
                                color="#888"
                            ),
                            padding="24px",
                            border="1px solid #333",
                            border_radius="8px",
                            width="100%"
                        ),
                        rx.box(
                            rx.heading("What types of companies use DuskUI?", size="4", margin_bottom="8px"),
                            rx.text(
                                "We work with companies of all sizes, from innovative startups to Fortune 500 enterprises. "
                                "Our platform serves companies across various industries including fintech, healthcare, "
                                "e-commerce, and more.",
                                size="3",
                                color="#888"
                            ),
                            padding="24px",
                            border="1px solid #333",
                            border_radius="8px",
                            width="100%"
                        ),
                        spacing="4",
                        width="100%",
                        max_width="800px",
                        margin="0 auto"
                    ),
                    padding="64px 32px",
                    width="100%"
                ),

                # CTA SECTION
                rx.box(
                    rx.box(
                        rx.heading("Ready to Start Your Journey?", size="8", text_align="center", margin_bottom="16px"),
                        rx.text(
                            "Join thousands of developers who have already found their dream jobs through DuskUI. "
                            "Create your profile today and let opportunities come to you.",
                            size="4",
                            text_align="center",
                            color="#888",
                            margin_bottom="32px",
                            max_width="600px",
                            margin_x="auto"
                        ),
                        rx.hstack(
                            rx.button(
                                "Create Free Account",
                                bg="#3b82f6",
                                color="white",
                                padding="16px 32px",
                                size="4",
                                border_radius="8px"
                            ),
                            rx.button(
                                "View Demo",
                                bg="transparent",
                                color="white",
                                border="1px solid #666",
                                padding="16px 32px",
                                size="4",
                                border_radius="8px"
                            ),
                            spacing="4",
                            justify="center"
                        ),
                        padding="64px 32px",
                        text_align="center"
                    ),
                    bg="linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%)",
                    border_radius="12px",
                    margin="32px 0"
                ),

                # FOOTER
                rx.box(
                    rx.vstack(
                        rx.hstack(
                            rx.box(
                                rx.hstack(
                                    rx.image(src="/DuskUI.ico", width="32px", height="auto"),
                                    rx.heading("DuskUI", size="4"),
                                    spacing="2"
                                ),
                                rx.text(
                                    "Connecting the world's best developers with amazing opportunities.",
                                    size="3",
                                    color="#888",
                                    margin_top="8px",
                                    max_width="300px"
                                ),
                                width="25%"
                            ),
                            rx.box(
                                rx.heading("Product", size="3", margin_bottom="16px"),
                                rx.vstack(
                                    rx.text("Features", size="2", color="#888"),
                                    rx.text("Pricing", size="2", color="#888"),
                                    rx.text("API", size="2", color="#888"),
                                    rx.text("Documentation", size="2", color="#888"),
                                    spacing="2",
                                    align="start"
                                ),
                                width="25%"
                            ),
                            rx.box(
                                rx.heading("Company", size="3", margin_bottom="16px"),
                                rx.vstack(
                                    rx.text("About", size="2", color="#888"),
                                    rx.text("Blog", size="2", color="#888"),
                                    rx.text("Careers", size="2", color="#888"),
                                    rx.text("Contact", size="2", color="#888"),
                                    spacing="2",
                                    align="start"
                                ),
                                width="25%"
                            ),
                            rx.box(
                                rx.heading("Legal", size="3", margin_bottom="16px"),
                                rx.vstack(
                                    rx.text("Privacy", size="2", color="#888"),
                                    rx.text("Terms", size="2", color="#888"),
                                    rx.text("Security", size="2", color="#888"),
                                    rx.text("Cookies", size="2", color="#888"),
                                    spacing="2",
                                    align="start"
                                ),
                                width="25%"
                            ),
                            spacing="4",
                            width="100%",
                            align="start"
                        ),
                        rx.divider(color="#333", margin="32px 0"),
                        rx.hstack(
                            rx.text("© 2024 DuskUI. All rights reserved.", size="2", color="#666"),
                            rx.spacer(),
                            rx.hstack(
                                rx.icon("twitter", size=20, color="#666"),
                                rx.icon("github", size=20, color="#666"),
                                rx.icon("linkedin", size=20, color="#666"),
                                spacing="4"
                            ),
                            width="100%",
                            align="center"
                        ),
                        spacing="4",
                        width="100%"
                    ),
                    padding="48px 32px",
                    border_top="1px solid #333",
                    width="100%"
                ),

                spacing="0",
                width="100%",
            ),
            bg="black",
            color="white",
            min_height="100vh",
            width="100%"
        ),
        type="always",
        scrollbars="vertical",
        style={"height": "100vh"},
        width="100%"
    )


app = rx.App()
app.add_page(index)
// Spatial Mechanics Course Configuration
export const spatialMechanicsConfig = {
  courseTitle: "Spatial Mechanics",
  courseDescription: "Analysis and design of three-dimensional mechanical systems through real-world mechatronic applications",
  totalLessons: 6,
  
  lessons: [
    {
      id: 1,
      title: "Kinematic Joints and Degrees of Freedom in 3D Systems",
      slug: "kinematic-joints-degrees-freedom",
      system: "Modular Robot Joint Library",
      duration: "120 minutes",
      difficulty: "Intermediate"
    },
    {
      id: 2,
      title: "Planar Transformations and Mathematical Foundations", 
      slug: "planar-transformations-foundations",
      system: "2D Planar Robot (SCARA-type)",
      duration: "135 minutes",
      difficulty: "Intermediate"
    },
    {
      id: 3,
      title: "3D Rotation Matrices and Spatial Transformations",
      slug: "spatial-rotations-transformations", 
      system: "6-DOF Industrial Robot Arm",
      duration: "150 minutes",
      difficulty: "Advanced"
    },
    {
      id: 4,
      title: "Elementary Matrix Methods and Link Modeling",
      slug: "matrix-methods-link-modeling",
      system: "Stewart Platform (Hexapod)",
      duration: "145 minutes", 
      difficulty: "Advanced"
    },
    {
      id: 5,
      title: "Advanced Spatial Mechanisms Analysis",
      slug: "advanced-spatial-mechanisms",
      system: "Humanoid Robot Hand",
      duration: "160 minutes",
      difficulty: "Expert"
    },
    {
      id: 6,
      title: "Computer Simulation and System Integration",
      slug: "computer-simulation-integration",
      system: "Multi-Robot Coordination System", 
      duration: "140 minutes",
      difficulty: "Expert"
    }
  ],

  prerequisites: [
    "Linear Algebra (Matrix operations, vector spaces)",
    "Trigonometry and Complex Numbers", 
    "Basic Planar Mechanics",
    "Programming fundamentals (for simulation lessons)"
  ],

  learningOutcomes: [
    "Analyze degrees of freedom in complex 3D mechanical systems",
    "Apply transformation matrices for spatial motion representation",
    "Design kinematic chains using systematic matrix methods", 
    "Simulate multi-body spatial mechanisms computationally",
    "Optimize spatial mechanisms for real-world applications"
  ]
};